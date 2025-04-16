import re

import data_fetcher


ANIMAL_FILE_PATH = "animals_data.json"
INPUT_HTML_FILE = "animals_template.html"
OUTPUT_HTML_FILE = "animals.html"
KEYWORD_PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def get_animal():
    """ Prompt user for animal """
    while True:
        animal_name = input("Enter a name of an animal: ").strip()
        if animal_name and re.match(r'^[A-Za-z ]+$', animal_name):
            return animal_name
        print("Invalid input. Please enter a valid animal name.")


def get_animal_data(animal):
    """ Returns the animal data from API """
    data = data_fetcher.fetch_data(animal)
    if not data:
        print(f"No data found for the given animal: {animal}.")
    return data


def build_animal_cards_html(animals_data):
    """ Generates HTML from filtered animal data. """
    output = ['<ul class="cards">']

    for animal in animals_data:
        name = animal.get('name', 'Unknown')
        diet = animal.get('characteristics', {}).get('diet', 'Unknown')
        location = ' '.join(animal.get('locations', [])) if 'locations' in animal else 'Unknown'
        animal_type = animal.get('characteristics', {}).get('type', 'Unknown')
        skin_type = animal.get('characteristics', {}).get('skin_type', 'Unknown')

        output.append(f"""
        <li class="cards__item">
          <div class="card__title">{name}</div>
          <div class="card__text">
            <ul>
              <li><strong>Diet:</strong> {diet}</li>
              <li><strong>Location:</strong> {location}</li>
              <li><strong>Type:</strong> {animal_type}</li>
              <li><strong>Skin Type:</strong> {skin_type}</li>
            </ul>
          </div>
        </li>
        """)

    output.append('</ul>')

    return '\n'.join(output)

def build_animal_not_found_card_html(animal_name):
    output =  f"""
                <ul class="cards">
                <li class="cards__item">
                  <div class="card__title">{animal_name}</div>
                  <div class="card__text">
                     This name does not match any animal in the Database.</div>
                  </div>
                </li>
                </ul>
                """
    return output


def replace_keyword_in_html(input_file, keyword, replacement, output_file):
    """
    Reads an HTML file, replaces a keyword with a specified string,
    and optionally saves the modified content to a new file.
    """
    try:
        # Read the HTML file
        with open(input_file, "r", encoding="utf-8") as file:
            html_content = file.read()

        # Replace the keyword with the given string
        modified_html = html_content.replace(keyword, replacement)

        # Save to output file if specified
        if output_file:
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(modified_html)
            print(f"Success: HTML file '{output_file}' has been created successfully.")

        return modified_html
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():

    animal_name = get_animal()

    # Get data
    animal_data = get_animal_data(animal_name)

    # Generate HTML
    if animal_data:
        formatted_data = build_animal_cards_html(animal_data)
    else:
        formatted_data = build_animal_not_found_card_html(animal_name)
    # Get new html file
    replace_keyword_in_html(INPUT_HTML_FILE, KEYWORD_PLACEHOLDER, formatted_data, OUTPUT_HTML_FILE)


if __name__ == '__main__':
    main()

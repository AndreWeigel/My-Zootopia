import json
import requests

from config import API_URL, API_KEY


ANIMAL_FILE_PATH = "animals_data.json"
INPUT_HTML_FILE = "animals_template.html"
OUTPUT_HTML_FILE = "animals.html"
KEYWORD_PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"

def get_animal():
    """ Prompt user for animal """
    animal_name = input("Enter a name of an animal: ").strip()
    if animal_name:
        return animal_name
    print("Invalid input. Please enter a valid animal name.")
    return animal_name

def fetch_data_from_api(animal_name):
    """ Fetches animal data from an API """
    full_api_url = API_URL + f"?name={animal_name}"

    try:
        response = requests.get(full_api_url, headers={"X-Api-Key": API_KEY})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return []


def get_animal_data(animal_name):
    """ Returns the animal data from API """
    return fetch_data_from_api(animal_name)



def get_filter(animals_data):
    """ Filter animal data by skin type."""
    skin_types = set([animal.get('characteristics', {}).get('skin_type') for animal in animals_data])
    # for handling missing data
    skin_types.add("Other")

    # Display available skin types to the user
    print("Available skin types:", ', '.join(skin_types))

    while True:
        # Ask user to select a skin type
        selected_skin_type = input("Enter a skin type from the list above: ")

        if selected_skin_type not in skin_types:
            print(f"Invalid choice. Please select a valid skin type from the list.")
            continue
        else:
            return selected_skin_type


def filter_animal_data(animals_data, selected_skin_type):
    """ Filters animal data based on the selected skin type. """
    filtered_data = []
    for animal in animals_data:
        skin_type = animal.get('characteristics', {}).get('skin_type')

        if selected_skin_type == "Other":
            if skin_type is None:
                filtered_data.append(animal)
        elif skin_type == selected_skin_type:
            filtered_data.append(animal)

    return filtered_data


def generate_html(animals_data):
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

    # Get user-selected filter
    #selected_skin_type = get_filter(animal_data)

    # Filter data
    #filtered_data = filter_animal_data(animal_data, selected_skin_type)

    # Generate HTML
    formatted_animal_data = generate_html(animal_data)

    # Get new html file
    replace_keyword_in_html(INPUT_HTML_FILE, KEYWORD_PLACEHOLDER, formatted_animal_data, OUTPUT_HTML_FILE)


if __name__ == '__main__':
    main()

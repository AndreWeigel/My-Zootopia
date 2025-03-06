import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def get_animal_data():
    """ Returns the animal data from JSON file """
    animals_data = load_data('animals_data.json')
    output = ['<ul class="cards">']

    for animal in animals_data:
        name = animal.get('name')
        diet = animal.get('characteristics', {}).get('diet')
        location = ' '.join(animal.get('locations', [])) if 'locations' in animal else None
        animal_type = animal.get('characteristics', {}).get('type')

        # Skip printing if any of the values are missing
        if None in (name, diet, location, animal_type):
            continue

        output.append(f"""
        <li class="cards__item">
            <div class="card__title">{name}</div>
            <div class="card__text">
                <ul>
                <li><strong>Diet:</strong> {diet}</li>
                <li><strong>Location:</strong> {location}</li>
                <li><strong>Type:</strong> {animal_type}</li>
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

        return modified_html
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    # Get data
    animal_data = get_animal_data()

    # define paths and keyword
    keyword = '__REPLACE_ANIMALS_INFO__'
    input_file = 'animals_template.html'
    output_file = 'animals.html'

    # Get new html file
    replace_keyword_in_html(input_file, keyword, animal_data, output_file)


if __name__ == '__main__':
    main()
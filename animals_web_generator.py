import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')
print(animals_data[0].keys())
for animal in animals_data:
    name = animal.get('name')
    diet = animal.get('characteristics', {}).get('diet')
    location = ' '.join(animal.get('locations', [])) if 'locations' in animal else None
    animal_type = animal.get('characteristics', {}).get('type')

    # Skip printing if any of the values are missing
    if None in (name, diet, location, animal_type):
        continue

    print(f"""
Name: {name}
Diet: {diet}
Location: {location}
Type: {animal_type}
    """)
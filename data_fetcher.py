import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_KEY")

def fetch_data(animal_name):
    """Fetches the animals data for the animal 'animal_name'"""
    full_api_url = f"{API_URL}?name={animal_name}"

    try:
        response = requests.get(full_api_url, headers={"X-Api-Key": API_KEY})
        response.raise_for_status()

        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

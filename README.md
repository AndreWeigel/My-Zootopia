# Animal Info HTML Generator

This project lets you search for animals and generates an HTML page with their details fetched from a public API.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/animal-info-html-generator.git
   cd animal-info-html-generator
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your API key:
   ```
   API_KEY='your_api_key_here'
   ```

## Usage
To use this project, simply run:
```bash
python animals_web_generator.py
```
Follow the prompt to enter an animal name. The program will generate an `animals.html` file with relevant information.

## Files
- `main.py` – Main script
- `data_fetcher.py` – API handler
- `animals_template.html` – HTML layout with a placeholder
- `animals.html` – Final generated output
- `.env` – Stores your API key (excluded from git)

## Contributing
We welcome contributions! To contribute:
- Fork the repository
- Create a new branch
- Make your changes
- Submit a pull request


# Professors Info Scraper

This project is a web scraping tool designed to extract and parse information from professor-related websites. The tool allows users to input a website URL, scrape the content, clean it, and then parse it based on user-defined descriptions. The parsed results can be exported in various formats such as CSV, JSON, or saved to a database.

## Features

- **Website URL Input**: Users can input the URL of the website they want to scrape.
- **Export Format Selection**: Users can choose the format in which they want to export the parsed results (CSV, JSON, Database).
- **Scrape Website**: Scrapes the website content and extracts the body content.
- **Clean Content**: Cleans the extracted body content.
- **View DOM Content**: Allows users to view the cleaned DOM content.
- **Parse Content**: Parses the cleaned content based on user-defined descriptions.
- **Export Parsed Results**: Exports the parsed results in the selected format.

## How to Use

1. **Input the Website URL**: Enter the URL of the website you want to scrape in the provided text input field.
2. **Select Export Format**: Choose the desired export format (CSV, JSON, Database) from the dropdown menu.
3. **Scrape the Website**: Click the "Scrape Site" button to start scraping the website. The cleaned DOM content will be displayed in an expandable text area.
4. **Describe Parsing Requirements**: Enter a description of what you want to parse from the cleaned content in the provided text area.
5. **Parse the Content**: Click the "Parse Content" button to parse the content based on your description. The parsed results will be displayed.
6. **Export Parsed Results**: Depending on the selected export format, you can download the parsed results as a CSV or JSON file, or save them to a database (coming soon).

## Dependencies

- `langchain_ollama`
- `streamlit` (imported as `st`)
- `pandas` (imported as `pd`)
- `json`

## Example
To use the Professors Info Scraper, follow these steps:

1. **Set Up the Environment**: Ensure you have all the necessary dependencies installed, including `langchain_ollama`, `streamlit`, `pandas`, and `json`.

2. **Run the Streamlit App**: Use the command `streamlit run main.py` to start the application.

3. **Input the Website URL**: Enter the URL of the website you want to scrape in the provided text input field.

4. **Select Export Format**: Choose the desired export format (CSV, JSON, Database) from the dropdown menu.

5. **Scrape the Website**: Click the "Scrape Site" button to start scraping the website. The cleaned DOM content will be displayed in an expandable text area.

6. **Describe Parsing Requirements**: Enter a description of what you want to parse from the cleaned content in the provided text area.

7. **Parse the Content**: Click the "Parse Content" button to parse the content based on your description. The parsed results will be displayed.

8. **Export Parsed Results**: Depending on the selected export format, you can download the parsed results as a CSV or JSON file, or save them to a database (coming soon).

This tool is designed to make it easy to extract and parse information from professor-related websites, providing flexibility in how the results are exported.

## Future Work
- [ ] Save parsed results to a database
- [ ] Add more parsing options
- [ ] Add more export options
- [ ] Add more website examples



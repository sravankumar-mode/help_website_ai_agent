# AI-powered Q&A Agent

## Description

This repository contains the implementation of an AI-powered question-answering agent designed to process and analyze documentation from help websites. The agent is capable of accurately answering user queries about product features, integrations, and functionality. 

This project is an AI-powered Q&A agent that scrapes content from a given URL, stores it in a JSON format, and allows users to ask questions based on the scraped content. The AI agent uses the Gemini API to provide answers to user queries.

---

## Setup Instructions

1. **Clone the repository**:
2. **Create a virtual environment** (optional but recommended):
3. **Install dependencies**:
4. **Set up environment variables**:
Make sure to set up any required environment variables (e.g., API keys, configuration values).


---

## Dependencies

- `selenium` for web scraping and interaction with web pages.
- `beautifulsoup4` for parsing HTML content.
- `requests` for HTTP requests and URL validation.
- `argparse` for command-line argument parsing.
- `logging` for logging and debugging.
- `gemini` for AI response generation (assumed based on the code).
- `os` for handling environment variables and file paths.

To install dependencies, use the following command:
pip install -r requirements.txt


---

## Usage Examples

1. **Scrape content from a URL and start the Q&A session**:
   Run the main script with the `--url` argument pointing to the target URL to scrape:

Example: 
python main.py --url "https://example.com"

2. **Interact with the AI agent**:
After running the script, you can ask the AI agent questions based on the scraped content:

Example: 
Ask a question: What is the main topic of the page?

4. **Exit the session**:
Type `exit` to stop the program:

Example: 
Ask a question: exit


---

## Design Decisions

- **Selenium and BeautifulSoup**: The project uses Selenium to load dynamic content from web pages and BeautifulSoup to parse the HTML and extract relevant content. This combination allows us to handle both static and JavaScript-rendered pages.

- **Logging**: Logs are generated throughout the application using Python's `logging` module for easy debugging and monitoring.

- **Error Handling**: The script includes error handling for network issues, invalid URLs, and failed scraping attempts, ensuring the agent doesn't crash unexpectedly.

- **Modular Design**: The project is divided into multiple modules like `scrape_code.py` for scraping, `validate_url.py` for URL validation, and `prompt.py` for generating instructions, making the code modular and easier to maintain.

---

## Known Limitations

- **Limited URL Depth**: The scraping process is limited to scraping a maximum of 100 URLs and 100,000 characters. This can be adjusted in the `scrape_urls_and_content` function.

- **Dynamic Content**: Pages with highly dynamic content that heavily rely on JavaScript might not be fully scraped, as Selenium might not always be able to extract all content if the page requires additional user interaction.

- **Error Handling**: While there is basic error handling, network issues or inaccessible URLs can still cause the scraping process to fail or produce incomplete results.

- **API Limitations**: The AI agent relies on external APIs (e.g., Gemini) for responding to user queries. If the API has downtime or rate limits, the response may be affected.

- **Environment-Specific Issues**: Some Chrome options (e.g., headless mode) may not work correctly in certain environments (e.g., in Docker, without a display server). Adjust the options as necessary based on your environment.

---

## Contribution

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.





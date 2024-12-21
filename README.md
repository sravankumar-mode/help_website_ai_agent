# AI-powered Q&A Agent

## Description

This repository contains the implementation of an AI-powered question-answering agent designed to process and analyze documentation from help websites. The agent is capable of accurately answering user queries about product features, integrations, and functionality. 

This project is an AI-powered Q&A agent that scrapes content from a given URL, stores it in a JSON format, and allows users to ask questions based on the scraped content. The AI agent uses the Gemini API to provide answers to user queries.

---

## Setup Instructions

1. **Clone the repository**:
   git clone https://github.com/sravankumar-mode/help_website_ai_agent.git

2. **Create a virtual environment** (optional but recommended):
   python -m venv venv source venv/bin/activate # On Windows use venv\Scripts\activate

3. **Install dependencies**:
   pip install -r requirements.txt

4. **Set up environment variables**:
   Make sure to set up the required environment variables, including the API key and the model name.
   Get your GEMINI API KEY [HERE](https://aistudio.google.com/app/apikey?_gl=1*1x804wt*_ga*MTIyNzg2MjE2NS4xNzI4NDQ4MDU3*_ga_P1DBVKWT6V*MTczNDc4NjA3Ny4xMC4xLjE3MzQ3ODYwODQuNTMuMC4xMjkzMjA1OTgw): 

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

## Code Files

### `config.py`
Contains configuration settings, including environment variables and API keys. This file is responsible for setting up the necessary configurations for the application.

### `prompt.py`
Generates the instructions and format for the AI agent's responses. This file contains the logic to structure the agent's responses based on the scraped content.

### `validate_url.py`
Validates whether a given URL is reachable and responds without errors. It uses `requests.head` to check the URL's status before attempting to scrape the content.

### `scrape_code.py`
Handles the actual web scraping process using Selenium and BeautifulSoup. This file scrapes URLs and content from a web page and stores the extracted data in a structured format.

### `GEMINI_test.py`
This file tests the Gemini API integration by sending requests to the API and receiving responses. It is used for evaluating the AI agent's ability to generate answers based on the scraped content.

### `main.py`
The main entry point of the application, which controls the flow of the script. It accepts user input, scrapes content from the URL, and initiates the AI-powered Q&A agent to answer user queries.

---

## Contribution

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

---


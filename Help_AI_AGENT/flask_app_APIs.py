import json
import re
import logging
import os
from flask import Flask, request, jsonify
from scrap_code import scrape_urls_and_content, validate_url
from GEMINI_test import start_chat, respond

# Suppress TensorFlow warnings
os.environ['PYTHONWARNINGS'] = 'ignore'

# Configure logging
logging.basicConfig(
    filename='ai_agent.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
)

# Initialize Flask app
app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    """
    Endpoint to scrape the content of a provided URL and return the scraped data as a JSON response.
    The user provides a URL in the POST request body.
    """
    data = request.json
    if not data or 'url' not in data:
        return jsonify({'error': 'URL is required'}), 400

    start_url = data['url']

    # Log the user's provided URL with IST time
    logging.info(f"INFO: User's URL: {start_url}")

    # Validate the input URL
    is_valid, error_message = validate_url(start_url)
    if not is_valid:
        logging.error(f"Error: {error_message}")
        return jsonify({'error': error_message}), 400

    # Proceed with scraping if the URL is valid
    result_data = scrape_urls_and_content(start_url)

    # Extract the domain name or part of the URL for the file name
    domain_name = re.sub(r'[^a-zA-Z0-9]', '_', start_url.split('//')[-1].split('/')[0])
    file_name = f'scraped_data_{domain_name}.json'

    # Write the results to a JSON file
    with open(file_name, 'w') as file:
        json.dump(result_data, file, indent=4)
        logging.info(f"Data saved to: {file_name}")

    return jsonify({'message': 'Scraping successful', 'file_name': file_name, 'data': result_data}), 200


@app.route('/ask', methods=['POST'])
def ask_question():
    """
    Endpoint to ask a question to the chat agent based on the previously scraped data.
    The user provides a question and the scraped data file in the POST request body.
    """
    data = request.json
    if not data or 'file_name' not in data or 'question' not in data:
        return jsonify({'error': 'Both file_name and question are required'}), 400

    file_name = data['file_name']
    question = data['question']

    # Start a chat session based on the file name (scraped data)
    chat_session = start_chat(file_name)

    # Get the response to the user's question
    query_answer = respond(chat_session, question)

    logging.info(f"INFO: User's Query: {question}")
    logging.info(f"INFO: Response: {query_answer}")

    return jsonify({'answer': query_answer}), 200


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)

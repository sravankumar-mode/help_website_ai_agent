import json
import argparse
import re
from scrap_code import scrape_urls_and_content, validate_url
from GEMINI_test import start_chat, respond
import logging
import os

# Suppress Python warnings
os.environ['PYTHONWARNINGS'] = 'ignore'

# Configure logging to capture information and errors
logging.basicConfig(
    filename='ai_agent.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',  # Log format including timestamp
)
# Main program execution
if __name__ == "__main__":

    # Log the user's provided URL with IST time
    logging.info(f"INFO: New User with new URL.")

    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="AI-powered Q&A agent.")
    parser.add_argument('--url', required=True, help="The help website URL to process.")
    args = parser.parse_args()

    START_URL = args.url

    # Log the user's provided URL with IST time
    logging.info(f"INFO: User's URL: {START_URL}")

    # Validate the input URL
    is_valid, error_message = validate_url(START_URL)

    # If the URL is invalid, log the error and terminate the program
    if not is_valid:
        print(f"Error: {error_message}")
        logging.error(f"Error: {error_message}")
        exit(1)

    # If the URL is valid, proceed with scraping its content
    result_data = scrape_urls_and_content(START_URL)

    # Extract the domain name or part of the URL for the file name
    domain_name = re.sub(r'[^a-zA-Z0-9]', '_', START_URL.split('//')[-1].split('/')[0])
    file_name = f'scraped_data_{domain_name}.json'

    print('file name:', file_name)

    # Save the scraped data to a JSON file
    with open(file_name, 'w') as file:
        json.dump(result_data, file, indent=4)  # Indented for readability
        print("Data saved to: ", file_name)

    # Start a chat session
    chat_session = start_chat(file_name)

    # Loop to allow the user to interact with the AI
    while True:
        # Get the user input (query)
        query = input("#########################################\nAsk a question: ( or type 'exit')\n")
        
        # If the user types 'exit', break the loop and end the program
        if query.lower() == "exit":
            print("Exiting...")
            break

        # Log the user's query to track what they are asking
        logging.info(f"INFO: User's Query: {query}")

        # Get the AI response for the user's query
        query_answer = respond(chat_session, query)
        print('\n', query_answer)
    
    # Log the completion of the task
    logging.info(f"INFO: The task is finished")
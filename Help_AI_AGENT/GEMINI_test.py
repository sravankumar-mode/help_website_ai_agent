import google.generativeai as genai
import json
from prompt import *
from config import API_KEY, MODEL_NAME

# Configure the API key for Google Generative AI
genai.configure(api_key = API_KEY)

def load_json(file_path):
    """
    Load the contents of a JSON file.

    This function opens a JSON file from the given path, reads its contents, 
    and parses it into a Python dictionary.

    Args:
        file_path (str): The path to the JSON file to load.

    Returns:
        dict: The parsed data from the JSON file.
    """

    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to start the chat session
def start_chat(json_file_path):
    
    """
    Start a chat session using the data from a specified JSON file.

    This function loads the JSON data from the given file, generates 
    instructions using the `get_instructions` function, and then initializes 
    the Google Generative AI model with these instructions. It returns 
    a chat session object to interact with the model.

    Args:
        json_file_path (str): The path to the JSON file containing the website data.

    Returns:
        ChatSession: An initialized chat session object for communication with the model.
    """

    # Load the JSON file containing data
    json_data = load_json(json_file_path)

    # Generate instructions based on the JSON data
    instruction = get_instructions(json_data)

    # Initialize the generative model with the specified configuration
    model = genai.GenerativeModel(
        model_name = MODEL_NAME,
        generation_config={
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        },
        system_instruction= instruction
    )
    
    # Start and return the chat session
    return model.start_chat()

# Send prompt to the model and get the response
def respond(chat_session, prompt):
    """
    Send a prompt to the chat session and receive the model's response.

    This function sends the provided prompt to the active chat session and 
    returns the model's generated response. If the prompt is empty, it returns 
    an error message.

    Args:
        chat_session (ChatSession): The chat session object where the prompt will be sent.
        prompt (str): The text prompt to send to the model.

    Returns:
        str: The model's response to the prompt, or an error message if the prompt is empty.
    """
    
    if prompt.strip():  # Ensure the prompt is not empty
        response = chat_session.send_message(prompt)
        return response.text
    else:
        return "Error: The prompt is empty!"

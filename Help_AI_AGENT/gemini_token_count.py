import os
import google.generativeai as genai

class FileCharacterAndTokenCounter:
    def __init__(self, api_key: str, model_name: str):
        """
        Initializes the counter with the API key and model name for token calculation.

        This constructor sets up the API key and model name needed to configure 
        the Google Generative AI client and prepares the model for use in 
        token counting.

        Args:
            api_key (str): The API key for accessing the Google Generative AI service.
            model_name (str): The model name to be used in token calculation.
        """
        self.api_key = api_key
        self.model_name = model_name
        self.model = None
        self.configure_and_set_model()

    def configure_and_set_model(self):
        """
        Configures the Generative AI client and sets the model.

        This method uses the provided API key to configure the Google Generative AI client 
        and then sets the model for counting tokens based on the provided model name.
        """

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name=self.model_name)

    def count_characters(self, file_path: str) -> int:
        """
        Counts the number of characters in the specified file.

        This method reads the contents of the specified file and returns the total 
        number of characters in the file. It also returns the content of the file as a string.

        Args:
            file_path (str): The path to the file to be processed.

        Returns:
            tuple: A tuple where the first element is the character count (int) and the second 
                   element is the file's content (str).
        """

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return len(content), content

    def count_tokens(self, content: str) -> int:
        """
        Counts the tokens in the given content using the configured model.

        This method uses the configured Google Generative AI model to count the number of 
        tokens in the given content.

        Args:
            content (str): The content for which token count is required.

        Returns:
            int: The number of tokens in the content.
        """

        return self.model.count_tokens(content)

    def process_files(self, directory: str):
        """
        Processes all JSON files in the specified directory, printing character and token counts.

        This method scans the given directory for all JSON files, and for each file, it calculates
        the character count and token count, printing the results. It handles any errors that may 
        occur while processing the files.

        Args:
            directory (str): The directory containing the JSON files to be processed.
        """
        
        for file_name in os.listdir(directory):
            if file_name.endswith(".json"):
                file_path = os.path.join(directory, file_name)
                try:
                    char_count, content = self.count_characters(file_path)
                    token_count = self.count_tokens(content)
                    print(f"File: {file_name} | Characters: {char_count} | Tokens: {token_count}")
                except Exception as e:
                    print(f"Error processing file {file_name}: {e}")

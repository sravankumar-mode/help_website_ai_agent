"""
config.py

This file contains configuration settings such as the API key and model name.
These values are used to authenticate and specify the machine learning model 
for your application.

Make sure to replace the placeholders with your actual API key and model name 
before using this configuration file.

Usage:
    - Import the variables from this file into your main application script
      to access the API key and model name.
      
    Example:
        from config import API_KEY, MODEL_NAME
        print(API_KEY)        # Access the API key
        print(MODEL_NAME)     # Access the model name

Note:
    It is recommended to keep this file secure and not to share it publicly as 
    it may contain sensitive information like API keys.
"""

# API Key for authentication with the service.
API_KEY = "AIzaSyAkmY6thIF97OPIkCZ3oSaqm0bKjEas2cc"

# Model name to specify the ML model to use in the application.
MODEL_NAME = "gemini-1.5-flash"
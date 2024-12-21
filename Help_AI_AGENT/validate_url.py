from urllib.parse import urlparse, urlunparse
import requests
import os

# Suppress Python warnings
os.environ['PYTHONWARNINGS'] = 'ignore'

def normalize_url(url):
    """
    Normalize the URL by removing fragments and ensuring consistent trailing slashes.

    This function processes the provided URL by removing any fragment (the part after the '#') 
    and ensures that the URL has a consistent format with or without a trailing slash at the end 
    of the path.

    Args:
    url (str): The URL to be normalized.

    Returns:
    str: The normalized URL with the fragment removed and consistent trailing slashes.
    """

    parsed = urlparse(url)
    # Remove the fragment
    url_without_fragment = parsed._replace(fragment='')

    # Ensure consistent trailing slash (or no trailing slash)
    normalized_path = url_without_fragment.path.rstrip('/')  # Remove trailing slash if it exists
    url_without_fragment = url_without_fragment._replace(path=normalized_path)

    return urlunparse(url_without_fragment)

def validate_url(url):
    """
    Validate the provided URL by sending a HEAD request and checking the response status.

    This function attempts to send a HEAD request to the provided URL and evaluates the server's 
    response. It returns a boolean indicating whether the URL is reachable and a message 
    indicating any errors encountered.

    Args:
    url (str): The URL to be validated.

    Returns:
    tuple: A tuple containing:
        - bool: True if the URL is valid and accessible, False otherwise.
        - str: A message describing the outcome or any error encountered.
    """
    try:
        response = requests.head(url, timeout=5)
        if response.status_code < 400:
            return True, None
        else:
            return False, f"URL returned an error: {response.status_code}"
    except requests.exceptions.ConnectionError:
        return False, "Failed to connect to the URL. Check if the domain exists or your internet connection."
    except requests.exceptions.Timeout:
        return False, "The request timed out. Please try again later."
    except requests.exceptions.RequestException as e:
        return False, f"An error occurred: {e}"
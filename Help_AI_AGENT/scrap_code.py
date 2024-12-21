from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from validate_url import *
import os

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppresses TensorFlow info and warning logs

def init_driver():
    """
    Initializes a headless Chrome WebDriver with various performance and logging optimizations.

    This function configures Chrome options to run in a headless mode (no GUI), with GPU and sandboxing disabled for performance.
    It also suppresses logs and disables unnecessary features that might cause issues in specific environments like Docker.

    Returns:
    webdriver.Chrome: A Selenium WebDriver object configured with the specified options.
    """

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless Chrome
    chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    chrome_options.add_argument("--no-sandbox")  # Disable sandboxing (needed in some environments)
    chrome_options.add_argument("--log-level=3")  # Suppress all but fatal Chrome logs
    chrome_options.add_argument("--disable-logging")  # Disable logging
    chrome_options.add_argument("--v=0")  # Set verbosity to minimum
    chrome_options.add_argument("--disable-features=MediaStream")  # Disable media features that cause FFmpeg warnings
    chrome_options.add_argument("--remote-debugging-port=0")  # Prevent the debug logs from showing
    chrome_options.add_argument("--disable-software-rasterizer")  # Disable software rasterizer to avoid WebGL issues
    chrome_options.add_argument("--disable-gl-extensions")  # Disable unnecessary OpenGL extensions
    chrome_options.add_argument("--no-sandbox")  # Disable sandboxing (useful in some environments like Docker)
    chrome_options.add_argument("--disable-software-rasterizer")  # Disable software rasterizer
    chrome_options.add_argument("--disable-accelerated-2d-canvas")  # Disable 2D canvas acceleration
    chrome_options.add_argument("--disable-accelerated-graphics")  # Disable graphics acceleration entirely
    chrome_options.add_argument("--disable-features=VizDisplayCompositor")  # Disable advanced rendering features
    
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Function to scrape URLs and content from a page using Selenium
def scrape_urls_and_content(start_url, max_urls=100, max_chars=100000):
    """
    Scrapes content and URLs from a given starting URL using Selenium and BeautifulSoup.

    This function uses Selenium to load web pages, extracts the text content and title of each page,
    and finds links to other pages. It continues scraping until the specified maximum number of URLs 
    or character limit is reached, storing the scraped data in a dictionary.

    Args:
    start_url (str): The URL to start scraping from.
    max_urls (int, optional): The maximum number of URLs to scrape (default is 100).
    max_chars (int, optional): The maximum number of characters of content to scrape (default is 100000).

    Returns:
    dict: A dictionary where keys are the normalized URLs, and values are dictionaries containing the 
          'title' and 'content' of the corresponding page. The content is the extracted text from the page.
    """
    try:
        validate_url(start_url)
    except ValueError as e:
        print(f"Validation Error: {e}")
        return {}

    driver = init_driver()
    visited = set()
    urls_to_scrape = [start_url]
    data = {}
    total_characters = 0

    while urls_to_scrape and len(data) < max_urls and total_characters < max_chars:
        current_url = urls_to_scrape.pop(0)
        normalized_url = normalize_url(current_url)
        if normalized_url in visited:
            continue
        visited.add(normalized_url)

        try:
            # Use Selenium to load the page
            driver.get(current_url)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )

            # Get the page content and parse with BeautifulSoup
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            title = soup.title.text if soup.title else 'No title'
            content = ' '.join(soup.stripped_strings)  # Get all text and strip excess whitespace

            # Check if adding this content will exceed the character limit
            if total_characters + len(title) + len(content) > max_chars:
                print(f"Stopping: Adding this URL will exceed {max_chars} characters.")
                break

            # Store data and update character count
            data[normalized_url] = {'title': title, 'content': content}
            total_characters += len(title) + len(content)

            # Find and normalize new URLs
            links = soup.find_all('a', href=True)
            for link in links:
                href = link['href']
                full_url = normalize_url(urljoin(current_url, href))
                if full_url not in visited and full_url not in urls_to_scrape:
                    urls_to_scrape.append(full_url)

            print(f"Scraped URL: {current_url} (Total characters: {total_characters})")

        except Exception as e:
            print(f"Error scraping {current_url}: {e}")

    driver.quit()
    return data
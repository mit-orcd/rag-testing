import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Set the base URL and folder where the markdown files will be saved
base_url = ""
output_folder = "orcd_docs"
page_list_file = "orcd_files.txt"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def save_page_as_md(url, content):
    """Save page content as a markdown file"""
    # Create a valid filename by replacing invalid characters
    filename = url.split("/")[-2] # nextline is empty, could also just strip
    filepath = os.path.join(output_folder, f"{filename}.md")
    
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Saved: {filepath}")

def get_page_content(url):
    """Fetch and extract the content of a page"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status codes
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract the main content from the page, e.g., paragraphs
        page_content = ""
        for paragraph in soup.find_all("p"):
            page_content += paragraph.get_text() + "\n\n"
        
        return page_content
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def download_specific_pages(base_url, page_names):
    """Download only the pages listed in the page_names file"""
    for page_name in page_names:
        page_name = page_name.strip()  # Remove any surrounding whitespace/newlines
        if not page_name:
            continue  # Skip empty lines
        
        # Construct the full URL for each page
        page_url = urljoin(base_url, page_name)
        # print("url", page_url)       
        # Fetch and save the page content
        content = get_page_content(page_url)
        if content:
            # print("True")
            save_page_as_md(page_url, content)

def load_page_names(file_path):
    """Load the list of page names from a file"""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()

# Load the page names from the file
page_names = load_page_names(page_list_file)

# Download the specific pages
download_specific_pages(base_url, page_names)


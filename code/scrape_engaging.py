import os
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://engaging-web.mit.edu/eofe-wiki/'
base_url = 'https://engaging-web.mit.edu'

# Folder to save the pages
folder = '../satori_docs'
visited = []
# Create the folder if it doesn't exist
if not os.path.exists(folder):
    os.makedirs(folder)

# Function to scrape and download pages
def scrape_and_download(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <a> tags under <ul> with class 'topics'
        topics = soup.find('ul', class_='topics') # class_= 'topics
        if topics:
            links = topics.find_all('a', href=True)
            for link in links:
                href = link['href']
                if href.startswith('/'):
                    href = base_url + href
                print(f'Downloading {href}...')
                response = requests.get(href)
                # print("href", href)
                soup = BeautifulSoup(response.text, 'html.parser')
                text = soup.get_text(strip=True)
                filename = href.split('/')[-2] + '.md'
                with open(os.path.join(folder, filename), 'w') as f:
                    f.write(text)
                print(f'Saved {filename} to {folder}/')


        # Find all <a> tags on the page to scrape other pages
        links = soup.find_all('a', href=True)
        for link in links:
            href = link['href']
            if href.startswith('/'):
                href = url + href
            if href.startswith('#'):  # ignore anchor links
                continue
            if href not in [url, url + '/'] and href not in visited:
                print("hrefs", href)
                # print("visited", visited)
                visited.append(href)
                scrape_and_download(href)
    except Exception as a:
        print(a)
        print("A file failed.")

# Start scraping and downloading pages
scrape_and_download(url)
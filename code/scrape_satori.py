import os
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
base_url = 'https://mit-satori.github.io/'
visited = []

# Folder to save the pages
folder = '../satori_docs'
global recursion_depth
recursion_depth = 0

# Create the folder if it doesn't exist
if not os.path.exists(folder):
    os.makedirs(folder)

# Function to scrape and download pages
def scrape_and_download(url):
    global recursion_depth

    if recursion_depth > 1:
        return 
    
    print(recursion_depth)

    try:
        print("hi")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

# assume 'soup' is a Beautiful Soup object
        # Find all <a> tags under <ul> with class 'topics'
        if recursion_depth==0:
            links = [a['href'] for a in soup.find_all('a', class_='reference internal')]
        if recursion_depth==1:
            links = [a['href'] for a in soup.find_all('a')]
        if links:
            for link in links:
                base_link = link.split('#')[0]
                if base_link not in visited:
                    visited.append(base_link)
                    try: 
                        if recursion_depth==0:
                            filename = link.split('.')[0] + '.md'
                        if recursion_depth==1:
                            filename = link.split('.')[0] + '.md'
                        
                        link = url + link
                        print(f'Downloading {link}...')
                        response_page = requests.get(link)
                        # print("href", href)
                        soup_page = BeautifulSoup(response_page.text, 'html.parser')
                        text = soup_page.get_text(strip=True)
                        with open(os.path.join(folder, filename), 'w', encoding='utf8', errors='ignore') as f:
                            f.write(text)
                        print(f'Saved {filename} to {folder}/')

                        # add all hrefs on the links page
                        recursion_depth += 1  
                        # print("i got far")
                        scrape_and_download(link)
                    except Exception as a:
                        print(a)
                        print("A file failed.")

    except Exception as a:
        print("large fail")
    

# Start scraping and downloading pages
scrape_and_download(base_url)
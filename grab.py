import requests
from bs4 import BeautifulSoup
import re

def fetch_data(url):
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

def extract_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find all headers and paragraphs in the HTML content
    headers = soup.find_all(re.compile(r'^h\d$'))  # Matches h1, h2, h3, etc.
    paragraphs = soup.find_all('p')
    content = []

    # Extract text from headers and paragraphs
    for header, paragraph in zip(headers, paragraphs):
        content.append((header.get_text(), paragraph.get_text()))

    return content

if __name__ == "__main__":
    url = "https://overwatch.fandom.com/wiki/Reaper#articleComments"
    html_content = fetch_data(url)
    if html_content:
        content = extract_content(html_content)
        for header, paragraph in content:
            print(f"{header}\n{paragraph}\n")












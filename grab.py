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
    content = []

    # Extract text from headers and associated paragraphs
    for header in headers:
        # Find the parent element that encompasses the header and its associated content
        parent = header.find_parent()
        # Extract all paragraphs within the parent element
        paragraphs = parent.find_all('p')
        # Combine paragraphs' text into a single string
        paragraph_text = '\n'.join(paragraph.get_text() for paragraph in paragraphs)
        # Append the header and paragraph text as a tuple to the content list
        content.append((header.get_text(), paragraph_text))

    return content

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Overwatch_(video_game)"
    html_content = fetch_data(url)
    if html_content:
        content = extract_content(html_content)
        with open('output.txt', 'w', encoding='utf-8') as f:
            for header, paragraph in content:
                f.write(f"{header}\n{paragraph}\n\n")
        print("Output saved to output.txt")














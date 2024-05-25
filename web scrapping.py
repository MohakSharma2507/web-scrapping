import urllib.request

# Replace with the desired URL
url = "https://mohaksharma2507.github.io/my_portfolio/"

with urllib.request.urlopen(url) as response:
  # Read the byte data
  html_bytes = response.read()
  
  # Decode bytes to string using UTF-8 encoding (common for webpages)
  html_string = html_bytes.decode("utf-8")

# Now you have the HTML content of the webpage as a string
# print(html_string)

from bs4 import BeautifulSoup

# Assuming you have the HTML string stored in 'html_string'

soup = BeautifulSoup(html_string, 'html.parser')

# Now you can use BeautifulSoup methods to navigate and extract data

# Example: Extract all text within the paragraph tags
paragraphs = soup.find_all('p')
paragraph_text = []
for paragraph in paragraphs:
  paragraph_text.append(paragraph.text.strip())

print(paragraph_text)


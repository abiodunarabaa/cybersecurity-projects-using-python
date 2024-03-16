import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage to scrape
url = 'https://abiodunarabaa.github.io'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all links on the webpage
links = soup.find_all('a')

# Extract and print the href attribute of each link
for link in links:
    href = link.get('href')
    print(href)


# Import the requests library to send HTTP requests and the BeautifulSoup class from the BeautifulSoup library to parse HTML content.
# Define the URL of the webpage we want to scrape (url).
# Send an HTTP GET request to the URL using requests.get() and store the response in the response variable.
# Parse the HTML content of the webpage using BeautifulSoup and store the result in the soup variable.
# Use the find_all() method of BeautifulSoup to find all <a> (anchor) tags, which represent links on the webpage.
# Ierate over each link, extract the value of the href attribute using the get() method, and print it.
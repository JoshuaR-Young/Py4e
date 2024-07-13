import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Function to follow links and find the last name
def follow_links(start_url, position, count):
    current_url = start_url

    for i in range(count):
        # Read the HTML from the current URL
        html = urllib.request.urlopen(current_url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')

        # Retrieve all anchor tags
        tags = soup('a')
        if len(tags) < position:
            return None

        # Find the link at the specified position
        link = tags[position - 1].get('href', None)
        if link is None:
            return None

        # Print the URL being retrieved
        print(f"Retrieving: {link}")

        # Move to the next URL
        current_url = link

    # Read the last page to get the last name
    html = urllib.request.urlopen(current_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # The last name is expected to be in the <h1> tag
    last_name = soup.find('h1').text
    return last_name

# Input data
start_url = input('Enter URL: ')
position = int(input('Enter position: '))
count = int(input('Enter count: '))

# Execute the function to follow links
last_name = follow_links(start_url, position, count)
print(f"Last name in sequence: {last_name}")

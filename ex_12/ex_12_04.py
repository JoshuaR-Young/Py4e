import urllib.request, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ')
try:
    response = urllib.request.urlopen(url)
    data = response.read()
except urllib.error.URLError as e:
    print('Failed to retrieve URL: {e.reason}')
    exit()

#Parse the HTML to Extract <p> tags
soup = BeautifulSoup(data, 'html.parser')
p_tags = soup.find_all('p')

#Count number of <p> tags
p_count = len(p_tags)

#Display <p> tags count
print(f'The number of Paragraph <p> tags is: {p_count}')
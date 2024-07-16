import urllib.request
import xml.etree.ElementTree as ET

url = 'https://py4e-data.dr-chuck.net/comments_2054099.xml'

# Fetch the data from the URL
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')

# Print the data length
data_length = len(data)
print('Retrieved', data_length, 'characters')

# Parse the XML data
tree = ET.fromstring(data)
counts = tree.findall('.//count')
nums = [int(count.text) for count in counts]

print('Count:', len(nums))
print('Sum:', sum(nums))

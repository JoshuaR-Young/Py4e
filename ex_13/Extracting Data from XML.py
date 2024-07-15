import xml.etree.ElementTree as ET

# Update the file_path variable with the actual path to your XML file
file_path = 'comments_2054099.xml'

# Read the data from the file
with open(file_path, 'r') as file:
    data = file.read()

# Print the data length
data_length = len(data)
print('Retrieved', data_length, 'characters')

# Parse the XML data
tree = ET.fromstring(data)
counts = tree.findall('.//count')
nums = [int(count.text) for count in counts]

# Print the results
print('Count:', len(nums))
print('Sum:', sum(nums))

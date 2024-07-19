import urllib.request
import json

url = input('Enter location: ')

#Retrieve the data from the URL
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

#Parse the JSON data
try:
    js = json.loads(data)
except:
    js = None

#Initialize sum and count variables
total = 0
count = 0

#Check if 'comments' key is in JSON data
if 'comments' in js:
    for comment in js['comments']:
        total += int(comment['count'])
        count += 1

#Print the count of comments and the sum of comment counts
print('Count:', count)
print('Sum:', total)

import urllib.request, urllib.error

#Step 1: Retrieve the document from a URL
url = input('Enter URL: ')
try:
    response = urllib.request.urlopen(url)
    data = response.read()
except urllib.error.URLError as e:
    print(f'Failed to retrieve URL: {e.reason}')
    exit()

#step 2: Diplay up to 3000 characters
decoded_data = data.decode('utf-8')
print(decoded_data[:3000])

#Step 3: Count the overall number of characters in the document
print(f'\nTotal number of characters in the document: {len(decoded_data)}')
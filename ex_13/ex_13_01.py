import urllib.request
import urllib.parse
import json
import sys

# Service URL for the geojson API
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter location (or type "exit" to quit): ')
    if address.lower() == 'exit':
        print('Exiting the program.')
        sys.exit()  # Exiting the program
    if len(address) < 1:
        break

    # Construct the URL with the provided address
    url = serviceurl + urllib.parse.urlencode({'address': address, 'key': 42})
    print('Retrieving', url)
    
    try:
        # Open the URL and read the data
        response = urllib.request.urlopen(url)
        data = response.read().decode()
        print('Retrieved', len(data), 'characters')

        # Parse the JSON data
        js = json.loads(data)
    except Exception as e:
        print(f'Error retrieving or parsing data: {e}')
        continue

    # Check if the JSON data contains the 'status' field and if it is 'OK'
    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure To Retrieve ===')
        print(data)
        continue

    # Extract the country code safely
    try:
        country_code = js['results'][0]['address_components'][-1]['short_name']
        print('Country code:', country_code)
    except (IndexError, KeyError) as e:
        print('Country code not found or not applicable')

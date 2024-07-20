import urllib.parse, urllib.request
import json

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

while True:
    #Prompt for location
    address = input('Enter location: ')
    if len(address) < 1:  # Exit on empty input
        break

    #Encode the address properly for URL
    url = serviceurl + urllib.parse.urlencode({'q': address})
    print('Retrieving', url)

    #Retrieve data from the URL
    with urllib.request.urlopen(url) as response:
        data = response.read().decode()
        print('Retrieved', len(data), 'characters')

        #Parse JSON data
        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'features' not in js or len(js['features']) == 0:
            print('==== Failure To Retrieve ====')
            print(data)
            continue

        #Extract and print the plus code
        plus_code = js['features'][0]['properties'].get('plus_code')
        if plus_code:
            print('Plus code', plus_code)
        else:
            print('==== Plus Code Not Found ====')
            print(data)
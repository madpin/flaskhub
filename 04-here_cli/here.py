import os
import requests

def get_address(source_address):
    url = 'https://geocoder.api.here.com/6.2/geocode.json'
    ret = {}

    payload = {
        'app_id': os.environ.get('HERE_APP_ID'),
        'app_code': os.environ.get('HERE_APP_CODE'),
        'country': 'ireland',
        'street': source_address,
    }

    response = requests.get(url, params=payload)
    response.encoding = 'utf-8'

    if(response.ok):
            # print(response.content)
            return response.json()



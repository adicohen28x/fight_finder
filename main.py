#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import os
import datetime
import requests
from dotenv import load_dotenv
load_dotenv()

sheet_name = os.getenv("GOOGLE_SHEET_NAME")
sheet_url = os.getenv("SHEET_URL")
cities_get_url = os.getenv("CITY_CODE_URL")
kiwi_api = os.getenv("KIWI_KEY")
# getting cities names from sheet:
get_cities = requests.get(url=sheet_url)

cities_list = [item['city'] for item in get_cities.json()['prices']]

city_headers={
    "apikey":kiwi_api,
    "accept":"application/json"
}

cities_codes=[]
for i in cities_list:
    kiwi_get= requests.get(url=f"{cities_get_url}?term={i}", headers=city_headers)
    cities_codes.append(kiwi_get.json()['locations'][0].get('code'))

print(cities_codes)


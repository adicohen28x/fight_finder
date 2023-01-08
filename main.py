# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import os
import datetime
import requests
from data_manager import DataManager
from flight_data import FlightData
from dotenv import load_dotenv
from flight_search import FlightSearch
load_dotenv()
kiwi_api = os.getenv("KIWI_KEY")

kiwi_headers = {
    "apikey": kiwi_api,
    "accept": "application/json"
}

data_manage = DataManager()
fiightSearch = FlightSearch(kiwi_headers)
city_codes = fiightSearch.get_citycode(data_manage.cities_list)
fiightSearch.inputParams()
list_cities = ",".join(fiightSearch.citieCodes)
search_get=fiightSearch.search_get(list_cities)
print(search_get)
data_manage.updateIATA(city_codes,search_get)
# data_manage.priceUpdate(search_get)

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import os
import datetime
import requests
from flight_data import FlightData
from dotenv import load_dotenv
load_dotenv()
kiwi_api = os.getenv("KIWI_KEY")

kiwi_headers = {
    "apikey": kiwi_api,
    "accept": "application/json"
}

flightData = FlightData(kiwi_headers)
flightData.get_citycode()
print(flightData.citieCodes)

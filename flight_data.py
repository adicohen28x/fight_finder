import os
import datetime
import requests
from dotenv import load_dotenv
load_dotenv()


class FlightData:
    def __init__(self, headers) -> None:
        self.sheet_name = os.getenv("GOOGLE_SHEET_NAME")
        self.sheet_url = os.getenv("SHEET_URL")
        self.cities_get_url = os.getenv("CITY_CODE_URL")
        self.citieCodes = []
        self.cities = self.getSheet()
        self.kiwi_headers = headers

    def getSheet(self):
        # getting cities names from sheet:
        self.get_cities = requests.get(url=self.sheet_url)
        cities_list = [item['city']
                       for item in self.get_cities.json()['prices']]
        return cities_list

    def get_citycode(self):
        for i in self.cities:
            kiwi_get = requests.get(
                url=f"{self.cities_get_url}?term={i}", headers=self.kiwi_headers)
            self.citieCodes.append(kiwi_get.json()['locations'][0].get('code'))

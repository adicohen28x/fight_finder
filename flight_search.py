import os
import requests
import datetime
from dotenv import load_dotenv
load_dotenv()


class FlightSearch:
    def __init__(self, headers) -> None:
        self.flight_search = os.getenv("FLIGHT_SEARCH_URL")
        self.kiwi_headers = headers
        self.cities_get_url = os.getenv("CITY_CODE_URL")
        self.citieCodes = []
 
        
    def get_citycode(self,cities):
        for i in cities:
            kiwi_get = requests.get(
                url=f"{self.cities_get_url}?term={i}", headers=self.kiwi_headers)
            self.citieCodes.append(kiwi_get.json()['locations'][0].get('code'))
        return self.citieCodes

    def inputParams(self):
        # self.dayFrom = input("First date of range")
        # self.dayBack = input("Last date of range")
        self.dayFrom = "03/04/2023"
        self.dayBack = "03/06/2023"

    def search_get(self, flyTo):
        self.search_quary = {
            "fly_from": "TLV",
            "fly_to": flyTo,
            "date_from": self.dayFrom,
            "date_to": self.dayBack,
            "one_for_city": 1,
        }

        res_search = requests.get(
            url=self.flight_search, params=self.search_quary, headers=self.kiwi_headers)
        flight_list = [{"id": item.get("id"), "fromCode": item.get("cityCodeFrom"),"fromCity": item.get("cityFrom"), "toCode": item.get("cityCodeTo"),"toCity": item.get("cityTo"), "price": item.get(
            "price"), "duration": item.get("duration").get("total")} for item in res_search.json()["data"]]
        return flight_list
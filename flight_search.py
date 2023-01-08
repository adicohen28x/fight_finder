import os
import requests
import datetime
from dotenv import load_dotenv
load_dotenv()


class FlightSearch:
    def __init__(self,headers) -> None:
        self.flight_search = os.getenv("FLIGHT_SEARCH_URL")
        self.kiwi_headers = headers
        
    def inputParams(self):
        self.dayFrom = input("First date of range")
        self.dayBack = input("Last date of range")

    def search_get(self):

        
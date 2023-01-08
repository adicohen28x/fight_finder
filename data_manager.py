
import os
import datetime
import requests
from dotenv import load_dotenv
load_dotenv()


class DataManager:
    def __init__(self) -> None:
        self.sheet_name = os.getenv("GOOGLE_SHEET_NAME")
        self.sheet_url = os.getenv("SHEET_URL")
        self.cities_list= None
        self.table = self.getSheet()
        

    def getSheet(self):
        # getting cities names from sheet:
        res = requests.get(url=self.sheet_url)
        table = res.json()['prices']
        self.cities_list = [item['city']
                       for item in table]
        return table

    def updateIATA(self,city_codes,flight_list):
        
        bodyi = [{"city": row.get("city"), "iataCode": city_codes[index], "lowestPrice": row.get("lowestPrice")} for index,row in enumerate(self.table)]
        for i in range (len(self.table)):
            body = {
                "price":
                    bodyi[i]
            }
            print(f"{self.sheet_url}/{i+2}")
            print(body)
            response = requests.put(url=f"{self.sheet_url}/{i+2}", json=body)
            print(response.json())

    def priceUpdate(self, flight_list):
        pass
        
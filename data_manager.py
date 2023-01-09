
import os
import datetime
import requests
from operator import itemgetter
from dotenv import load_dotenv
from notification_manager import NotificationManager
load_dotenv()


class DataManager:
    def __init__(self) -> None:
        self.sheet_name = os.getenv("GOOGLE_SHEET_NAME")
        self.sheet_url = os.getenv("SHEET_URL")
        self.cities_list = None
        self.table = self.getSheet()
        self.notify = NotificationManager()

    def getSheet(self):
        # getting cities names from sheet:
        res = requests.get(url=self.sheet_url)
        print(res.status_code)
        table = res.json()['prices']
        self.cities_list = [item['city']
                            for item in table]
        return table

    def updateIATA(self, city_codes):
        bodyi = [{"city": row.get("city"), "iataCode": city_codes[index], "lowestPrice": row.get(
            "lowestPrice")} for index, row in enumerate(self.table)]
        bodyii = sorted(self.table, key=itemgetter('city'))
        for i in range(len(self.table)):
            body = {
                "price":
                    bodyii[i]
            }
            print(body)
            response = requests.put(url=f"{self.sheet_url}/{i+2}", json=body)
            # print(response.json())

    def priceUpdate(self, search):
        for row in self.table:
            body = {"city": row.get("city"), "iataCode": row.get("iataCode"), "lowestPrice": row.get("lowestPrice"), "id": row.get("id")}
            for flight in search:
                if flight.get("toCity") == body.get("city"):
                    city = flight.get("toCity")
                    if flight.get("price") < body.get("lowestPrice"):
                        amount = flight.get("price")
                        date = flight.get('departure')[:10]
                        body["lowestPrice"] = flight.get("price")
                        self.notify.sendNotify(f"wow flight to {city} is only {amount}$ on {date}!!!")
                    else:
                        break
            body_to_sent = {"price": body}
            response = requests.put(url=f'{self.sheet_url}/{str(body.get("id"))}', json=body_to_sent)
            print(response.json())
import requests
import dotenv
import os

ZAR = "ZAR"
EUR = "EUR"
URL = "https://api.fastforex.io/fetch-one"

class ExchangeRate:
    # This class is responsible to make zar to Uero convention

    def __init__(self):
        dotenv.load_dotenv()
        self._api_key = os.getenv(key="FOREX")


    def convert_zar_to_eur(self, zar):

        headers = {
            "X-API-Key": self._api_key
        }

        params = {
            "from":ZAR,
            "to": EUR 
        }
        response = requests.get(url=URL, headers=headers, params=params)
        response.raise_for_status()

        # print(response.text)
        rate = response.json()["result"]["EUR"]
        total = round(self.multiply(zar, rate), 2)
        # print(total)
        return round(total)
    
    def convert_eur_to_zar(self, eur):
        headers = {
            "X-API-Key": self._api_key
        }

        params = {
            "from":EUR,
            "to": ZAR 
        }
        response = requests.get(url=URL, headers=headers, params=params)
        response.raise_for_status()

        # print(response.text)
        rate = response.json()["result"]["ZAR"]
        total = round(self.multiply(eur, rate), 2)
        # print(total)
        return round(total)

    def multiply(self, base, currency):
        return base * currency
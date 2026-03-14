import os
import dotenv
import requests

ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        dotenv.load_dotenv()
        self._api_key = os.getenv(key="API_KEY")
        self._api_secret = os.getenv(key="API_SECRET")
        self._token = self._get_new_token()

    
    def put_testing(self, data:dict) -> dict:
        '''
            This function is responsible for checking each an every data passed in has the iataCode available if not just pass in Testing for that data.
        '''
        code = data["iataCode"]
        if len(code) == 0:
            data["iataCode"] = "Testing"
        return data
    
    def _get_new_token(self):
        hearder = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
        "grant_type": "client_credentials",
        "client_id": self._api_key,
        "client_secret": self._api_secret
        }
        response = requests.post(url=ENDPOINT, headers=hearder, data=data)
        # print(response.text)
        response.raise_for_status()
        return response.json()["access_token"]
    
    def seach_iaticode(self, city):

        hearders = {
            "Authorization": f"Bearer {self._token}"
        }
        params = {
            "keyword": city,
            "max": 1,
            "include" : "AIRPORTS"
        }
        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        response =  requests.get(url=url, params=params, headers=hearders)
        response.raise_for_status()
        data = response.json()
        # print(response.text)
        # print(data)
        return data["data"][0]["iataCode"]
    

    def find_cheapest_flights(self, origin_code, destination_code, departure_date, adults=1):
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        params = {
            "originLocationCode": origin_code,
            "destinationLocationCode": destination_code,
            "departureDate": departure_date,
            "adults": adults,
            "max": 10
        }
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        print(response.text)
        return response.json()


    


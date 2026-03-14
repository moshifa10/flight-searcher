import requests
from flight_search import FlightSearch

class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self):
        search: FlightSearch = FlightSearch()
        self._token = search._token


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
        # print(response.text)
        return response.json()
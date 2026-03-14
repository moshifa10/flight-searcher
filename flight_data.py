import requests
from flight_search import FlightSearch

class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self):
        search: FlightSearch = FlightSearch()
        self._token = search._token


    def find_cheapest_flights(self, origin_code, destination_code, departure_date, adults=1):
        '''
            This function is responsible for finding destination and return all data
        '''
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

        try:
            response.json()["data"][0]
            # print(response.json()["data"][0])

        except IndexError:
            return None
        else:
            return response.json()["data"][0]
    
    def find_one_cheap_flight(data: list[dict])-> float:
        '''
            will find the cheapest and print out the cheapest from the list of the flight
        '''

        # for now I will have the constant cheap = 70
        cheap = 70
        got = False

        for flight in data:
            total = round(float(flight["price"]["grandTotal"]), 2)

            if cheap > total:
                cheap = total
                got = True

        if got:
            return cheap
        
        return False
    
    def validate_price(self, lower_price, actual_price) -> bool:
        '''
            If the price == data or < data[lowerstprice] -> True else False
        '''

        return False if float(actual_price) > float(lower_price) else True




    
        
    
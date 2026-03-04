import dotenv
import os
import requests

dotenv.load_dotenv()


#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


endpoint_sheet = os.getenv(key="END_POINT")

response = requests.get(url=endpoint_sheet)
response.raise_for_status()
print(response.text)




'''
APIs Required
Google Sheet Data Management - https://sheety.co/
Amadeus Flight Search API (Free Signup, Credit Card not required) - 
Amadeus Flight Offer Docs - https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference
Amadeus How to work with API keys and tokens guide - https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335
Amadeus Search for Airport Codes by City name - https://developers.amadeus.com/self-service/category/destination-experiences/api-doc/city-search/api-reference
Twilio Messaging (SMS or WhatsApp) API - https://www.twilio.com/docs/messaging/quickstart/python

Program Requirements
Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).
Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
If the price is lower than the lowest price listed in the Google Sheet then send an SMS (or WhatsApp Message) to your own number using the Twilio API.
The SMS should include the departure airport IATA code, destination airport IATA code, flight price and flight dates. e.g.
'''
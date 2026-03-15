import dotenv
import os
import requests
import data_manager 
import pprint
import flight_search
from flight_data import FlightData
from exchange_rate import ExchangeRate
from notification_manager import NotificationManager
dotenv.load_dotenv()

STARTING_POINT = "JNB"

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# call class and 
data =  data_manager.DataManager(url=os.getenv(key="END_POINT"))
sheety_data = data.get_data()
updated_sheety_data= []

# for i in sheety_data:
#     search = flight_search.FlightSearch()
#     updated_sheety_data.append(search.put_testing(i))

# pprint.pprint(sheety_data)


search = flight_search.FlightSearch()

flight_data = FlightData()
rate = ExchangeRate()
notification = NotificationManager()

# retrieve all emails from the google sheet form
sheety_emails_url = os.getenv(key="SHEETY_USERS")
response = requests.get(url=sheety_emails_url)
response.raise_for_status()
sheety_emails = [i["yourEmail?"] for i in response.json()["users"]]
# print(sheety_emails)

def iata_code():
    for i in sheety_data:
        if (i["iataCode"] == "" or i["iataCode"] == "Testing"):
            city = i["city"]
            iata_code = search.seach_iaticode(city=city)
            i["iataCode"] = iata_code
            success = data.put_data(body=i, id=i["id"])
            # print(iata_code)


for i in sheety_data:
    # print(i)
    print(f"Getting flights for {i["city"]} .....")
    cheapest_fligths = flight_data.find_cheapest_flights(
                            origin_code=STARTING_POINT,
                            destination_code=f"{i["iataCode"]}",
                            departure_date="2026-05-20"
                            )
    
    # validate
    if cheapest_fligths == None:
        print(f"No flight data")
        print(f"{i["city"]}: N/A")
        continue
    

    lowest_price = rate.convert_zar_to_eur(int(i["lowestPrice"]))
    validate = flight_data.validate_price(lower_price=lowest_price, actual_price=cheapest_fligths["price"]["grandTotal"])

    if validate:
        # print(f"R{i["lowestPrice"]} vs R{rate.convert_eur_to_zar(float(cheapest_fligths["price"]["grandTotal"]))}")
        converted = rate.convert_eur_to_zar(float(cheapest_fligths["price"]["grandTotal"]))
        segments= cheapest_fligths["itineraries"][0]["segments"]
        inbound_date, outbound_date =  " departure at ".join(segments[0]["departure"]["at"].split("T")), " arrive at ".join( segments[0]["arrival"]["at"].split("T"))
        
        print(f"{i["city"]}: R{converted}")
        for j in sheety_emails:
            notification.send_email(price=converted, departure=STARTING_POINT, arrival=i["iataCode"], inbound_date=inbound_date, outbound_date= outbound_date, email= j)

    else:
        # print(f"R{i["lowestPrice"]} vs R{float(cheapest_fligths["price"]["grandTotal"])}")
        print(f"No flight data")
        print(f"{i["city"]}: N/A")

# print(cheapest_fligths)



# print(search._token)

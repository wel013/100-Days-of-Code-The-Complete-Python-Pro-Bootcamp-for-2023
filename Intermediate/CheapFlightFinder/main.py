from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint
import requests


# ORIGIN_CITY_IATA = "LAX"

data_manager = DataManager()
flight_search = FlightSearch()


# retrieves everything stored in the sheet (inside "prices")
sheet_data = data_manager.get_destination_data()

# if iata is empry then need to fill it in
if sheet_data[0]["iataCode"] == '':
    for row in sheet_data:
        city = row['city']
        cityIATA = flight_search.get_destination_codes(city)
        row["iataCode"] = cityIATA
        data_manager.update_destination_codes(row)

# pprint(sheet_data)
# city_names = [row["city"] for row in sheet_data]
# data_manager.city_codes = flight_search.get_destination_codes(city_names)
# data_manager.update_destination_codes()
# sheet_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": int(round(float(data["lowestPrice"]), 0))
    } for data in sheet_data}


# tomorrow = datetime.now() + timedelta(days=1)
# six_month_from_today = datetime.now() + timedelta(days=6 * 30)

# for destination_code in destinations:
for i, destination_code in enumerate(destinations):
    if i >= 9:
        break
    details = destinations[destination_code]
    flight = flight_search.check_flights("LON", "London",
                                         destination_code,
                                         details['city'],
                                         details['price'],
                                         is_direct=False)

    if flight is None:
        print(
            f"There is not flight from London to {details['city']} that is lower than {details['price']}")

    else:
        user_numbers = data_manager.get_customer_number()
        for number in user_numbers:
            city_id = details['id']
            data_manager.update_price(city_id, flight.price)
            print(
                f"New cheap flight from London to {details['city']} that is lower than {details['price']}")
            # origin, origina_city, dest, dest_city, depart, return_date, price
            notification_manager = NotificationManager("LON", "London", destination_code, details['city'],
                                                       flight.out_date, flight.return_date, flight.price, flight.stop_overs, number)
            notification_manager.send_message()

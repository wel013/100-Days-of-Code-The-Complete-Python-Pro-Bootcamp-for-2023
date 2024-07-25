import requests
from pprint import pprint

# get_sheety_api = "https://api.sheety.co/618014cdc0e4d014e07e8904d965f0e4/entrFlightDeals/prices"
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/618014cdc0e4d014e07e8904d965f0e4/cheapFlightFinder2024/prices"
# SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/618014cdc0e4d014e07e8904d965f0e4/flightDeals/prices"

response = requests.get(url=SHEETY_PRICES_ENDPOINT)
data = response.json()
# pprint(data)


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint().
        # pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id  from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).

    def update_destination_codes(self, row):
        print("in updataing code")
        put_url = f"https://api.sheety.co/618014cdc0e4d014e07e8904d965f0e4/cheapFlightFinder2024/prices/{row['id']}"
        # for city in self.destination_data:
        new_data = {
            "price": {
                "iataCode": row["iataCode"]
            }
        }
        response = requests.put(
            url=put_url,
            json=new_data
        )
        print(response.text)

    def update_price(self, id, price):
        put_url = f"https://api.sheety.co/618014cdc0e4d014e07e8904d965f0e4/cheapFlightFinder2024/prices/{id}"
        # for city in self.destination_data:
        new_data = {
            "price": {
                "lowestPrice": price
            }
        }
        response = requests.put(
            url=put_url,
            json=new_data
        )
        print(response.text)

    def get_customer_emails(self):
        customers_endpoint = "https://api.sheety.co/618014cdc0e4d014e07e8904d965f0e4/entrFlightDeals/users"
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "<insert your url>"

response = requests.get(url=SHEETY_PRICES_ENDPOINT)
data = response.json()
# pprint(data)


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_number_list = []

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # pprint(data)
        return self.destination_data
    def update_destination_codes(self, row):
        print("in updataing code")
        put_url = f"<insert your url>"
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
        put_url = <insert yout endpoint>
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

    def get_customer_number(self):
        customers_endpoint = <insert your endpoint>
        response = requests.get(customers_endpoint)
        data = response.json()
        print(data)
        self.customer_number_list = [
            user['whatIsYourNumber?'] for user in data['users']]
        return self.customer_number_list


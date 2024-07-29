from pprint import pprint
from flight_data import FlightData
import requests
from datetime import datetime, timedelta
import os



class FlightSearch:

    def __init__(self):
        self.city_codes = []
        self._api_key = "/"
        self._api_secret = "/"
        self._token = self._get_new_token()

    def _get_new_token(self):
        TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
        # Header with content type as per Amadeus documentation
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id':  self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_destination_codes(self, city_name):
        print(city_name)
        # TODO: I always forget how to auth; check and remember
        headers = {"Authorization": f"Bearer {self._token}"}
        city_name_url = f'https://test.api.amadeus.com/v1/reference-data/locations/cities?keyword={city_name}&max=2'
        print("get destination codes triggered")
        try:
            response = requests.get(
                url=city_name_url, headers=headers)
            result = response.json()["data"][0]["iataCode"]
        except:
            print("DID NOT GET THE RIGHT RESPONSE")
        return result

    def check_flights(self, origin_city_code, origina_city, destination_city_code, destination_city, max_price, is_direct=True):
        flight_data = ""
        print(f"Check flights triggered for {destination_city_code}")
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        today = datetime.today()
        tomorrow = today + timedelta(days=1)
        date_180_days_later = tomorrow + timedelta(days=180)
        departure_start = tomorrow.strftime('%Y-%m-%d')
        departure_end = date_180_days_later.strftime('%Y-%m-%d')
        headers = {"Authorization": f"Bearer {self._token}"}
        if is_direct:
            query = {
                "originLocationCode": origin_city_code,
                "destinationLocationCode": destination_city_code,
                "departureDate": departure_start,
                "returnDate": departure_end,
                "adults": 1,
                "nonStop": "true",
                "max": 1,
                "maxPrice": max_price
            }
        else: 
            query = {
                "originLocationCode": origin_city_code,
                "destinationLocationCode": destination_city_code,
                "departureDate": departure_start,
                "returnDate": departure_end,
                "adults": 1,
                "nonStop": "false",
                "max": 1,
                "maxPrice": max_price
            }
        # print(query)
        response = requests.get(
            url=url,
            headers=headers,
            params=query,
        )
        # try:
        data = response.json()
        if len(data["data"]) != 0:

            # print(data["dictionaries"]["locations"])
            price = response.json()["data"][0]["price"]["grandTotal"]
            stops = len(data["data"][0]["itineraries"][0]['segments'])
            flight_data = FlightData(
                price=price,
                origin_city=origina_city,
                origin_airport=data["data"][0]["itineraries"][0]["segments"][0]["departure"]["iataCode"],
                destination_city=destination_city,
                destination_airport=data["data"][0]["itineraries"][0]["segments"][0]["arrival"]["iataCode"],
                out_date=departure_start,
                return_date=departure_end,
                stop_overs=stops-1
            )
        else:
            flight_data = None
        # except:
        #     print("SOME ERROR")
        return flight_data

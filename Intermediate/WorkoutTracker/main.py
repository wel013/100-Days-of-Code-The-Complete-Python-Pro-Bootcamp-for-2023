import requests
import os
from datetime import datetime

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
endpoint = os.environ["endpoint"]
basic_username = os.environ["basic_username"]
basic_password = os.environ["basic_password"]

bear_token = {"Authorization": "Bearer/"}
today = datetime.now()

exercise_ep = "https://trackapi.nutritionix.com/v2/natural/exercise"


post_req_body = {
 "query": input("Tell me which exercises you did: "),
 "gender": "female",
 "weight_kg": 63.5029,
 "height_cm": 168,
 "age": 23
}

header = {
 "x-app-id": APP_ID,
 "x-app-key": API_KEY
}

response = requests.post(url=exercise_ep, json=post_req_body, headers=header)

result = response.json()
print(f"Nutritionix API call: \n {result} \n")

# response.raise_for_status()
exercise_list = response.json()["exercises"]





#all keys need to be lowercased!
for exercise in exercise_list:
   exercise_dict = {
     "sheet1": {
        "date": today.strftime('%d/%m/%Y'),
        "time": today.strftime("%X"),
        "exercise": exercise['name'].title(),
        "duration": exercise['duration_min'],
        "calories": exercise['nf_calories']
     }
   }
   # r = requests.post(url=endpoint, json=exercise_dict, auth=(basic_username, basic_password))
   r = requests.post(url=endpoint, json=exercise_dict, headers=bear_token)
   print(f"Sheety Response: \n {r.text}")


   # print(r.text)
   # print(endpoint)

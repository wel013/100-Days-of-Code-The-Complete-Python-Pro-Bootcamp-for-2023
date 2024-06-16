import requests
from datetime import datetime
# created user on pixela
USERNAME = "wenqian"
TOKEN = "/"
#token is basically an api key and you can make it up yourselves
user_parameters = {
    "token": "/",
    "username": "wenqian",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

pixela_ep = "https://pixe.la/v1/users"
# response = requests.post(url=pixela_ep, json=user_parameters)
# print(response.text)
#{"message":"Success. Let's visit https://pixe.la/@wenqian , it is your profile page!","isSuccess":true}

# create graph
# to access this example:
# https://pixe.la/v1/users/wenqian/graphs/g1.html
graph_ep = "https://pixe.la/v1/users/wenqian/graphs"
graph_parameters = {
    "id": "g1",
    "name": "Did you read today?",
    "unit": "pages",
    "type": "int",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_ep, json=graph_parameters, headers=headers)
# print(response.text)

today = datetime.now()
#yyyyMMdd
value_ep = "https://pixe.la/v1/users/wenqian/graphs/g1"
value_parameters = {
    "date": today.strftime('%Y%m%d'),
    "quantity": str(input("how many pages did you read today?"))
}

response = requests.post(url=value_ep, json=value_parameters, headers=headers)
print(response.text)

#https://pixe.la/v1/users/wenqian/graphs/g1.html

update_ep = f"https://pixe.la/v1/users/wenqian/graphs/g1/{today.strftime('%Y%m%d')}"
update_param = {
    "quantity": "20"
}
# response = requests.post(url=value_ep, json=value_parameters, headers=headers)
# print(response.text)


delete_ep = f"https://pixe.la/v1/users/wenqian/graphs/g1/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_ep, headers=headers)
# print(response.text)

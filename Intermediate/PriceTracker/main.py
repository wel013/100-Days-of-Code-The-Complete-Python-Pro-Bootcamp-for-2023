import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import lxml

twilio_num = "+/"
account_sid = "/"
auth_token = "/"



TARGET_PRICE = replace with any number you want!
PRODUCT_URL = "Replace with anything you want!"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
accept_language = "en-US,en;q=0.9"
header = {
"Accept-Language":accept_language,
"User-Agent":user_agent
}
response = requests.get(url=PRODUCT_URL, headers=header)
response.raise_for_status()
PRODUCT_CONTENT = response.text
soup = BeautifulSoup(PRODUCT_CONTENT, "lxml")


price = soup.find(class_="rtx_option_subheading")
if price:
    # Extract the text and remove the currency symbol
    price_text = price.text.strip().replace('$', '')
    price_as_float = float(price_text)
    print(price_as_float)
else:
    print("Price not found.")



if price_as_float < TARGET_PRICE:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Subject: LOW PRICE \n\n the clear protein is now {price_as_float}. \n{PRODUCT_URL}",
        from_=twilio_num,
        to='+/'
    )
    print(message.status)






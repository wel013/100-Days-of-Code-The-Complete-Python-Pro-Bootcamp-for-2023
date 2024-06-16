import requests
from datetime import date
from datetime import timedelta
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

PRICE_API_KEY = "/"
NEWS_API_KEY = "/"

threshhold = 5

twilio_num = "+/"
account_sid = "/"
auth_token = "/"

today = date.today()
today_date = str(today)
# Yesterday date
yesterday = today - timedelta(days=1)
yesterday_date = str(yesterday)
# The day before yesterday date
ototoi = yesterday - timedelta(days=1)
ototoi_date = str(ototoi)
print(yesterday_date)
print(ototoi_date)

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={PRICE_API_KEY}"
r = requests.get(url)
r.raise_for_status()
data = r.json()

yesterday_price = float(data["Time Series (Daily)"][yesterday_date]["4. close"])
ototoi_price = float(data["Time Series (Daily)"][ototoi_date]["4. close"])

change_p: float = ((yesterday_price - ototoi_price) / yesterday_price) * 100


url_news = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}"
r_news = requests.get(url_news)
r_news.raise_for_status()
data_news = r_news.json()

articles_list = data_news["articles"]
articles_slice = articles_list[:3]



msg_list = [f"Headline: {article['title']} \n Brief: {article['content']}" for article in articles_slice]
print(msg_list)
if abs(change_p) >= threshhold:
    if change_p > 0:
        title = f"TSLA: 🔺{round(change_p)}%"
    elif change_p < 0:
        title = f"TSLA: 🔻{round(change_p)}%"
    client = Client(account_sid, auth_token)
    for article in msg_list:
        message = client.messages.create(
             body=f"{title} \n {article}",
             from_=twilio_num,
             to='+16265604141'
         )
    print(message.status)




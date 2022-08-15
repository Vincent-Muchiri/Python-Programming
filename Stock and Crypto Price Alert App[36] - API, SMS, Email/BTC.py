#btc-price-alert-app.py
import os

import requests
from os import environ, mkdir
from datetime import datetime, timedelta
import json
import math
from twilio.rest import Client

alphaVintage_key = os.environ['alphaVintage_key']

newsapi_key = os.environ['newsapi_key']

twilio_account_sid = os.environ['twilio_account_sid']
twilio_auth_token = os.environ['twilio_auth_token']

asset_sym = 'BTC'

newsapi_url = "https://newsapi.org/v2/everything?"
alphavantage_url = 'https://www.alphavantage.co/query?'

twilio_from_no = os.environ['twilio_from_no']
twilio_to_no = os.environ['twilio_to_no']

# TODO Define parameters
crypto_params = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": asset_sym,
    "market": "USD",
    "apikey": alphaVintage_key}

response = requests.get(alphavantage_url, params=crypto_params)
asset_data = response.json()

# TODO Create a folder named "data"
path = "./data"
try:
    mkdir(path)
except FileExistsError:
    pass

# TODO Get the current data
current_date = datetime.now().date()

# TODO Save the stock data to a json file
with open(f"{path}/{asset_sym}_{current_date}.json", mode="w") as stock_file:
    json.dump(asset_data, stock_file, indent=4)

# TODO Get the two recent dates as strings using the list and key methods
recent_date = list(asset_data["Time Series (Digital Currency Daily)"].keys())[0]
before_recent_date = list(asset_data["Time Series (Digital Currency Daily)"].keys())[1]

# TODO Get the closing price of recent and the day before
recent_close = float(asset_data["Time Series (Digital Currency Daily)"][f"{recent_date}"]["4b. close (USD)"])
before_recent_close = float(asset_data["Time Series (Digital Currency Daily)"][f"{before_recent_date}"]["4b. close (USD)"])
# print(recent_close, before_recent_close)

# TODO Test data
# recent_close = 25
# before_recent_close = 50

# TODO Get the percentage difference between the two
difference = abs(before_recent_close - recent_close)
# print(difference)
difference_perc = (difference / before_recent_close) * 100

# TODO Get news articles when the difference is greater or equal to five
if difference_perc >= 0.25:
    # TODO Make the heading
    if before_recent_close < recent_close:
        heading = f"{asset_sym}:🔺{difference_perc}%"
    elif before_recent_close > recent_close:
        heading = f"{asset_sym}:🔻{difference_perc}%"

    # TODO Define the parameters
    newsapi_params = {
        "q": asset_sym,
        "sortBy": "popularity",
        "language": "en",
        "from": before_recent_date,
        "to": recent_date,
        "apikey": newsapi_key,
        "pageSize": 3
    }

    # TODO Get the JSON data
    response = requests.get(newsapi_url, params=newsapi_params)
    news_data = response.json()

    # TODO Save the data in a JSON file
    # with open(f"{path}/{asset_sym}_news_{current_date}.json", mode="w") as news_file:
    #     json.dump(news_data, news_file, indent=4)

    # TODO Get the article list
    article_list = news_data['articles']

    # TODO Send text messages for each article
    for article in article_list:
        # TODO Get the heading and the content
        title = article['title']
        brief = article['description']

        # TODO Send the message
        client = Client(twilio_account_sid, twilio_auth_token)

        message_contents = f"{heading}\n" \
                           f"{title}\n" \
                           f"{brief}"

        # message = client.messages \
        #     .create(body=message_contents,
        #             from_=twilio_from_no,
        #             to=twilio_to_no)

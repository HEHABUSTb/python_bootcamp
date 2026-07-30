import os

import requests
from env import STOCK_API

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
API_KEY = STOCK_API

def get_daily_prices():
    endpoint = "https://www.alphavantage.co/query"

    params = {
        "function": "TIME_SERIES_DAILY",
        "apikey": API_KEY,
        "symbol": "TSLA",
        "outputsize": "compact",
    }

    response  = requests.get(endpoint, params=params)
    response.raise_for_status()

    data = response.json()
    dates = list(data["Time Series (Daily)"].keys())

    latest_date = dates[0]
    prev_date = dates[1]

    latest_day = data["Time Series (Daily)"][latest_date]
    prev_day  = data["Time Series (Daily)"][prev_date]

    print(latest_date)
    print(latest_day)
    print(latest_day['4. close'])

    print(prev_date)
    print(prev_day)
    print(prev_day['1. open'])

get_daily_prices()


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


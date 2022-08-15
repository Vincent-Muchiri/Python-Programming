import datetime
import random


days_of_the_week = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]

today = days_of_the_week[datetime.datetime.now().weekday()]

if today == "Thur":
    with open("quotes.txt", mode="r") as quotes_file:
        quotes = quotes_file.readlines()

    days_quote = random.choice(quotes)

    print(days_quote)
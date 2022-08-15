import datetime
import random
import smtplib

my_email = "tripiestands@gmail.com"
password = "F2i9lFnl8Wb0!C)"

# TODO Check the day today

days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]

day_index = datetime.datetime.now().weekday()
day = days_of_week[day_index]

# TODO Check whether today is Wednesday
if day == "Wed":
    # TODO Open text file and extract the data into a list
    with open("quotes.txt", mode="r") as quotes_file:
        quotes = quotes_file.readlines()

        wed_quote = random.choice(quotes)

# TODO Send email with quote message
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="vincentmuchiri.official@outlook.com",
                        msg=f"Subject:Wednesday Quote of The Day\n\n"
                            f"{wed_quote}")

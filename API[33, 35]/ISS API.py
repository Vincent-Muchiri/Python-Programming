import requests
from datetime import datetime
import time
import smtplib
import geocoder

# -----------------------------------------CONSTANTS AND VARIABLES -------------------------------------------------

MY_EMAIL = "tripiestands@gmail.com"
MY_PASSWORD = "Enter password"

# TODO Get the current location of the user using the IP address
geo = geocoder.ip('me')
current_location = geo.latlng

current_lat = current_location[0]
current_long = current_location[1]

parameters = {
    "lat": current_lat,
    "lng": current_long,
    "formatted": 0
}

# TODO Check whether it's day or night at a particular location using the SunriseSunset API
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

# TODO Extract the sunrise and sunset times from the JSON data in 24HR format
data = response.json()
# TODO Split the string to get the time
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

# TODO Separate the date and the time
sunset = sunset.split("T")

# TODO Get the time only
sunset = sunset[1]

# TODO Remove the microseconds
sunset = sunset.split("+")[0]
sunrise = sunrise.split("T")[1].split("+")[0]

# TODO Get the current time
current_time = datetime.now().time()


# TODO Get the position of ISS
def iss_position():
    iss_request = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_request.raise_for_status()
    iss_position_data = iss_request.json()

    iss_lat = float(iss_position_data["iss_position"]["latitude"])
    iss_long = float(iss_position_data["iss_position"]["longitude"])

    iss_long_lat = {
        "long": iss_long,
        "lat": iss_lat
    }
    return iss_long_lat

# TODO Test purposes
# LONGITUDE = iss_position()["long"]
# LATITUDE = iss_position()['lat']


# TODO Check the position of the ISS every 30 sec
while True:
    iss_long_lat = iss_position()

    # print(iss_long_lat)
    # print(current_location)

    # TODO Check whether the ISS is close to your location
    long_dif = abs(current_long - iss_long_lat["long"])
    lat_diff = abs(current_lat - iss_long_lat["lat"])

    current_hour = current_time.hour
    # current_hour = 20

    sunset_hour = int(sunset.split(":")[0])
    sunrise_hour = int(sunrise.split(":")[0])

    # TODO If the position of ISS is near by 5 degrees get the current hour, sunset and sunrise hour
    if long_dif <= 5 or lat_diff <= 5:
        # TODO Check whether its night time/after sunset and before sunrise
        if current_hour <= sunrise_hour or current_hour >= sunset_hour:
            # TODO Establish connection
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls() # Secure connection
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    to_addrs="vincentmuchiri1@gmail.com",
                    from_addr=MY_EMAIL,
                    msg="Subject:ISS Passing Above You\n\n"
                        "Look up!"
                )
        else:
            print("It's day time")
    else:
        print("ISS not close enough")
    # TODO Add a 30 second delay
    time.sleep(30)

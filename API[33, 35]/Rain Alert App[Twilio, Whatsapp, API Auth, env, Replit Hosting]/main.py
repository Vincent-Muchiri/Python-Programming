import requests
import os
import json
from datetime import datetime, timedelta
from twilio.rest import Client
# import pywhatkit

LONG = 37.014404
LAT = -1.101822

KEY = "4f8d0b9b29c3024b7ccb872efff7a70b"

# TODO Call the Twilio API
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACd8d21a162d64bcdbba53d8e76c711c0e"
auth_token = "7c67a13a2dcaa67ca75179fe585e38f8"

# TODO Call the weather API
url = f"https://api.openweathermap.org/data/2.5/onecall?" \
      f"lat={LAT}&" \
      f"lon={LONG}&" \
      f"exclude=current,minutely,daily,alerts&" \
      f"appid={KEY}"

# response = requests.get(url)
# response.raise_for_status()
#
# weather_api_data = response.json()
#
# # TODO Save the data in a JSON file
# try:
#     os.mkdir("data")
# except FileExistsError:
#     pass
#
# with open("./data/test.json", mode="w") as json_file:
#     json.dump(weather_api_data, json_file, indent=4)

# TODO Offline testing
with open("./data/test.json", mode="r") as json_file:
    weather_api_data = json.load(json_file)

will_rain = False

# TODO Get the data for the first 12 hrs
hourly_list = weather_api_data['hourly'][:13]
for hour_data in hourly_list:
    # hour_data = hourly_list[hour_index]
    weather_conditions_list = hour_data['weather']
    for condition in weather_conditions_list:
        weather_code = condition['id']
        # print(weather_code)
        if weather_code > 700:
            will_rain = True
            # TODO Get the timestamp and convert it to local time
            timestamp = hour_data['dt']
            time_dt = datetime.fromtimestamp(timestamp).time()

            # TODO Get the description
            weather_description = condition['description'].capitalize()

            # print(f"{weather_description} forecasted at {time_dt}. Carry an umbrella.")

            # TODO Send the SMS
            client = Client(account_sid, auth_token)

            message_contents = f"{weather_description} forecasted at {time_dt}. Carry an umbrella."
            from_no = '+19897873943'
            to_no = '+254798794666'

            message = client.messages \
                .create(
                    body=message_contents,
                    from_=from_no,
                    to=to_no
                )

            # TODO Send the Whatsapp message
            # TODO Get the current time and add 2 minutes to it
            sending_time = datetime.now() + timedelta(minutes=2)
            sending_time_hr = sending_time.hour
            sending_time_min = sending_time.minute

            # pywhatkit.sendwhatmsg(to_no,
            #                       message_contents,
            #                       sending_time_hr, sending_time_min)
            # pywhatkit.sendwhatmsg('+25479001219',
            #                       message_contents,
            #                       sending_time_hr, sending_time_min)
    break

# if will_rain:
#     print("Carry an umbrella")

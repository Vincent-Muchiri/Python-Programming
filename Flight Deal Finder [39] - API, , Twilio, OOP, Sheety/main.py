import requests
from twilio.rest import Client
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from pprint import pprint
import os
from datetime import datetime, timedelta
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

# -------------------------------------------- Variables and Constants -------------------------------------------------
SHEETY_BEARER_TOKEN = os.environ["SHEETY_BEARER_TOKEN"]

sheety_header = {
    'Authorization': f"Bearer {SHEETY_BEARER_TOKEN}"
}

KIWI_API_KEY = os.environ["KIWI_API_KEY"]
kiwi_api_header = {
    "apikey": KIWI_API_KEY
}

kiwi_location_query_params = {
    "term": "",
    "locale": "en-US",
    "location_types": "city"
}

get_sheety_endpoint = "https://api.sheety.co/8d71f9dad050e97aca87b3b97e94d5d9/pythonProgrammingGoogleSheetsApi/" \
                      "flightDealFinderDay39"
post_sheety_endpoint = "https://api.sheety.co/8d71f9dad050e97aca87b3b97e94d5d9/pythonProgrammingGoogleSheetsApi/" \
                       "flightDealFinderDay39"
put_sheety_endpoint = "https://api.sheety.co/8d71f9dad050e97aca87b3b97e94d5d9/pythonProgrammingGoogleSheetsApi/flightDealFinderDay39/[Object ID]"

TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_FROM_PHONE_NO = os.environ["TWILIO_FROM_PHONE_NO"]
TWILIO_TO_PHONE_NO = os.environ["TWILIO_TO_PHONE_NO"]

message_list = []


def get_sheet_data():
    # TODO Get Data from Google sheets
    test_get_response = requests.get(get_sheety_endpoint, headers=sheety_header)
    test_get_response.raise_for_status()
    sheet_data = test_get_response.json()
    # print(sheet_data)
    # pprint(sheet_data)

    # TODO Save the sheety data in a local json file
    with open("data/sheety data.json", mode="w") as json_file:
        json.dump(sheet_data, json_file, indent=4)

    # TODO Get the sheet data only
    sheet_data_list = sheet_data["flightDealFinderDay39"]
    # print(sheet_data_list)
    return sheet_data_list


def add_aita_code():
    sheet_data_list = get_sheet_data()
    # print(sheet_data_list)
    aita_dict = {}
    for row in sheet_data_list:
        if "iataCode" not in row or row["iataCode"] == "":
            # TODO Get the name of the city
            city_name = row['city']
            # print(city_name)

            # TODO Add the city name to the params
            kiwi_location_query_params["term"] = city_name
            # print(kiwi_location_query_params)

            # TODO Search for the IATA code of the city
            response = requests.get(url="https://tequila-api.kiwi.com/locations/query?",
                                    params=kiwi_location_query_params,
                                    headers=kiwi_api_header)
            response.raise_for_status()
            location_data_json = response.json()
            city_iata_code = location_data_json["locations"][0]["code"]

            # TODO Add the IATA codes to Google sheets
            row_data = {
                'flightDealFinderDay39': {
                    'iataCode': city_iata_code
                }
            }

            # TODO Get the row number
            row_number = row["id"]

            test_put_response = requests.put(
                f"https://api.sheety.co/8d71f9dad050e97aca87b3b97e94d5d9/pythonProgrammingGoogleSheetsApi/flightDealFinderDay39/{row_number}",
                json=row_data, headers=sheety_header)
            test_put_response.raise_for_status()


def send_message(message_list):
    # print(message_list)
    for message_contents in message_list:
        # print(message_contents)
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # TODO Send message
        try:
            message = client.messages.create(
                body="message_contents",
                from_=TWILIO_FROM_PHONE_NO,
                to=TWILIO_TO_PHONE_NO
            )
        except:
            print("Message failed to send")
        else:
            print("Message successfully sent!")
            print(message.sid)


def get_flight_data():
    destination_city = ""
    date_from = ""
    date_to = ""  # search flights up to this date (dd/mm/yyyy)
    return_from = ""  # min return date of the whole trip (dd/mm/yyyy)
    return_to = ""
    nights_in_dst_from = ""  # the minimal length of stay in the destination given in the fly_to parameter.
    nights_in_dst_to = ""
    flight_type = ""  # switch for oneway/round flights search - will be deprecated in the near future (until then, you have to use the round parameter if one from the nights_in_dst of return date parameters is given.)
    adults = 1
    children = 0
    infants = 0
    selected_cabins = ""  # Specifies the preferred cabin class. Cabins can be: M (economy), W (economy premium), C (business), or F (first class). There can be only one selected cabin for one call.
    curr = ""
    price_from = 0
    price_to = 0
    max_stopovers = 0
    sort = ""  # sorts the results by quality, price, date or duration. Price is the default value.
    asc = 1  # can be set to 1 or 0, default is 1 - from the cheapest flights to the most

    # The correct date format is dd/mm/YYYY, e.g. 29/05/2021

    # Accepts multiple values separated by a comma, these values might be airport codes, city IDs, two letter country codes, metropolitan codes and radiuses as well as a subdivision, region, autonomous_territory, continent and specials (Points of interest, such as Times Square).
    # flight_search_params = {
    #     "curr": "KES",
    #     "fly_from": "NRB",
    #     "fly_to": destination_city,
    #     "date_from": date_from,
    #     "date_to": date_to,
    #     "return_from": return_from,
    #     "return_to": return_to,
    #     "nights_in_dst_from": nights_in_dst_from,
    #     "nights_in_dst_to": nights_in_dst_to,
    #     "price_from": price_from,
    #     "price_to": price_to,
    #     "max_stopovers": max_stopovers,
    #     "sort": sort,
    #     "asc": asc
    # }
    departure_city = "LON"
    flight_search_params = {}
    flight_search_params["curr"] = "USD"
    flight_search_params["fly_from"] = departure_city
    flight_search_params["max_stopovers"] = 0  # Direct flight only
    flight_search_params["flight_type"] = "round"
    flight_search_params["nights_in_dst_from"] = 7
    flight_search_params["nights_in_dst_to"] = 28
    # Return between 7 and 28 days

    # TODO Get tomorrows date
    tomorrows_date = datetime.now().date() + timedelta(days=1)

    # TODO Convert the datetime object to a string
    tomorrows_date_str = tomorrows_date.strftime("%d/%m/%Y")
    flight_search_params["date_from"] = tomorrows_date_str

    # TODO Add 60 days from today's date and convert it to a string
    max_date = tomorrows_date + timedelta(days=60)
    max_date_str = max_date.strftime("%d/%m/%Y")
    flight_search_params["date_to"] = max_date_str

    # TODO Loop through the data from the Google sheet and create a dict
    sheet_data_list = get_sheet_data()
    # sheet_data_list = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
    #                    {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3}]
    # sheet_data_list = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]

    # TODO Initialize the dict
    flight_data_dict = {}
    destination_cities_list = []

    destination_city_dict = {}

    for row in sheet_data_list:
        # TODO Call the API
        destination_city_code = row["iataCode"]
        flight_search_params["fly_to"] = destination_city_code

        response = requests.get(
            url="https://tequila-api.kiwi.com/v2/search?",
            params=flight_search_params,
            headers=kiwi_api_header
        )
        response.raise_for_status()
        flight_data = response.json()
        # print(flight_data)

        # TODO Save the data to a json file
        with open(f"data/From {departure_city} to {destination_city_code}.json", mode="w") as json_flight_data_file:
            json.dump(flight_data, json_flight_data_file, indent=4)

        # TODO Add the tickets
        # flight_search_params[departure_city][destination_city_code] = flight_data["data"]
        # destination_city_dict = {}
        destination_city_dict[destination_city_code] = {}
        # TODO Add a list of dicts containing the route, fare, departure and arrival time
        tickets_data = flight_data["data"]
        # print(tickets_data)

        for ticket in tickets_data:
            message = ""

            # TODO Get the ticket price
            ticket_price = ticket["price"]
            lowest_price = row["lowestPrice"]
            # TODO Check whether the ticket price is less or equal to the one in Google sheets
            # print(row["lowestPrice"], ticket_price)
            if ticket_price > lowest_price:
                # TODO Get route data
                routes = ticket["route"]
                for route_details in routes:
                    # TODO Get the departure city name, departure airport IATA code, arrival city name,
                    #  arrival airport IATA code, outbound date, inbound date
                    departure_city_name = route_details["cityFrom"]
                    departure_airport_code = route_details["flyFrom"]
                    arrival_city_name = route_details["cityTo"]
                    arrival_airport_code = route_details["flyTo"]

                    # TODO Get the date and time and convert them to a string
                    departure_datetime_list = route_details["local_departure"].split("T")
                    arrival_datetime_list = route_details["local_arrival"].split("T")

                    departure_date = departure_datetime_list[0]
                    arrival_date = arrival_datetime_list[0]

                    departure_time = departure_datetime_list[1]
                    arrival_time = arrival_datetime_list[1]

                    # TODO Clean the time strings
                    departure_time = departure_time.removesuffix(".000Z")
                    arrival_time = arrival_time.removesuffix(".000Z")

                    # TODO Add the data to a string
                    message += f"\nLow price alert! " \
                               f"Only ${ticket_price} to fly from {departure_city_name}-{departure_airport_code} " \
                               f"to {arrival_city_name}-{arrival_airport_code}, " \
                               f"from {departure_date} to {arrival_date}."


                # TODO Get the booking link and append it to the list
                booking_link = ticket["deep_link"]

                # TODO Concatenate the message with the booking link
                message += f"\nTo book the trip, go to {booking_link}"

                # TODO Append the message to a list
                message_list.append(message)

                break

    # print(message_list)

    # TODO Send message
    send_message(message_list)


get_flight_data()

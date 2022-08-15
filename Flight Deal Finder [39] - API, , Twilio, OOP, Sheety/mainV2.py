from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

SHEET_NAME = "flightDealFinderDay39"

message_list = []

# TODO Get the sheet data
data_manager = DataManager()
sheet_data = data_manager.get_sheet_data(SHEET_NAME)

flight_search = FlightSearch()

# TODO Check whether all IATA codes are correct or exist
flight_search.get_iata_codes(sheet_data, SHEET_NAME)

# TODO Search for available flights
for row in sheet_data:
    flight_tickets = flight_search.search_flight(row)

    for ticket in flight_tickets:
        # print(ticket)
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
                flight_data = FlightData()
                message += flight_data.create_message(route_details, ticket_price)

            # TODO Get the booking link and append it to the list
            booking_link = ticket["deep_link"]

            # TODO Concatenate the message with the booking link
            message += f"\nTo book the trip, go to {booking_link}"

            # TODO Append the message to a list
            message_list.append(message)

# TODO Send the message via twilio
notification_messanger = NotificationManager()
notification_messanger.send_message(message_list)

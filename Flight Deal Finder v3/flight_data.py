class FlightData:
    """This class is responsible for structuring the flight data."""

    def create_message(self, route_details, ticket_price):
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
        message = f"\nLow price alert! " \
                       f"Only ${ticket_price} to fly from {departure_city_name}-{departure_airport_code} " \
                       f"to {arrival_city_name}-{arrival_airport_code}, " \
                       f"from {departure_date} to {arrival_date}."

        return message

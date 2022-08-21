import requests
import os
from datetime import datetime, timedelta
from data_manager import sheety_header


KIWI_API_KEY = os.environ["KIWI_API_KEY"]
kiwi_api_header = {
    "apikey": KIWI_API_KEY
}

kiwi_location_query_params = {
    "term": "",
    "locale": "en-US",
    "location_types": "city"
}

message_list = []


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    # TODO Find empty IATA code in Google sheets and add data to it from kiwi api
    def get_iata_codes(self, sheet_data: list, sheet_name: str):
        """
        Method that searches for empty IATA code in the Google sheets using the sheety GET method,\n
        searches for the code using the kiwi location endpoint by passing the city name from the sheet data\n
        and add the code using the PUT sheety endpoint
        :param search_data: row data stored in a list
        :param sheet_name: name of the sheet containing the city names
        """
        aita_dict = {}

        for row in sheet_data:
            if "iataCode" not in row or row["iataCode"] == "":
                # TODO Get the name of the city
                city_name = row['city']

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
                    sheet_name: {
                        'iataCode': city_iata_code
                    }
                }

                # TODO Get the row number
                row_number = row["id"]

                test_put_response = requests.put(
                    f"https://api.sheety.co/8d71f9dad050e97aca87b3b97e94d5d9/pythonProgrammingGoogleSheetsApi/flightDealFinderDay39/{row_number}",
                    json=row_data, headers=sheety_header)
                test_put_response.raise_for_status()

    # TODO Search for flights
    def search_flight(self, row: dict):
        """
        Searches for a flight based on the departure city, arrival city, maximum stopovers, trip type,
        maximum and minimum number of nights in destination
        :param row: Accepts the individual row data as a dict
        :return: Flight data
        """
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

        # TODO Initialize the dict
        flight_data_dict = {}
        destination_cities_list = []

        destination_city_dict = {}

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
        # with open(f"data/From {departure_city} to {destination_city_code}.json", mode="w") as json_flight_data_file:
        #     json.dump(flight_data, json_flight_data_file, indent=4)

        # TODO Add the tickets
        # flight_search_params[departure_city][destination_city_code] = flight_data["data"]
        # destination_city_dict = {}
        destination_city_dict[destination_city_code] = {}
        # TODO Add a list of dicts containing the route, fare, departure and arrival time
        tickets_data = flight_data["data"]
        # print(tickets_data)

        return tickets_data

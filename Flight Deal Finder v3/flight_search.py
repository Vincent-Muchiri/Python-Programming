import requests
import os
from tkinter import messagebox

# from data_managerV3 import sheety_header
KIWI_API_KEY = "x9Bvxwr3yQ6FOp2TrQchuNgYnv6RO4fy"

kiwi_api_header = {
    "apikey": KIWI_API_KEY
}

kiwi_location_query_params = {
    "term": "",
    "locale": "en-US",
    "location_types": "city"
}


class FlightSearch:

    def search_flight(self, search_dict: dict):
        """
        Searches for a flight based on the departure city, arrival city, maximum stopovers, trip type,
        maximum and minimum number of nights in destination
        :param search_dict: Accepts the individual row data as a dict
        :return: Flight data
        """

        # TODO Call the KIWI search api
        response = requests.get(
            url="https://tequila-api.kiwi.com/v2/search?",
            params=search_dict,
            headers=kiwi_api_header
        )
        response.raise_for_status()
        flight_search_results = response.json()

        tickets_data = flight_search_results["data"]

        return tickets_data

    def get_iata_code(self, location: str):
        kiwi_location_query_params["term"] = location

        response = requests.get(url="https://tequila-api.kiwi.com/locations/query?",
                                params=kiwi_location_query_params,
                                headers=kiwi_api_header)
        response.raise_for_status()
        location_data_json = response.json()

        city_iata_code = location_data_json["locations"][0]["code"]
        return city_iata_code

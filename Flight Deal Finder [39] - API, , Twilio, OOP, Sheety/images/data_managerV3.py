import requests
import os
import pandas
import threading

SHEETY_BEARER_TOKEN = os.environ["SHEETY_BEARER_TOKEN"]

sheety_header = {
    'Authorization': f"Bearer {SHEETY_BEARER_TOKEN}"
}

get_sheety_endpoint = "https://api.sheety.co/8d71f9dad050e97aca87b3b97e94d5d9/pythonProgrammingGoogleSheetsApi/" \
                      "flightDealFinderDay39"
post_sheety_endpoint = "https://api.sheety.co/8d71f9dad050e97aca87b3b97e94d5d9/pythonProgrammingGoogleSheetsApi/" \
                       "flightDealFinderDay39"
put_sheety_endpoint = "https://api.sheety.co/8d71f9dad050e97aca87b3b97e94d5d9/pythonProgrammingGoogleSheetsApi/" \
                      "flightDealFinderDay39/[Object ID]"


class DataManagerv3:
    def __init__(self):
        self.new_directory = "./data"
        if not os.path.exists(self.new_directory):
            os.mkdir(self.new_directory)

    def save_search_data(self, search_dict: dict):
        # TODO Save the dict to a treeview

        # TODO Save the dict in form of a CSV file locally
        search_param_dataframe = pandas.DataFrame(search_dict)
        search_param_dataframe.to_csv(f"{self.new_directory}/")

        # TODO Save the search dict to Google sheets

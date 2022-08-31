import requests
from os import path, mkdir, environ
import pandas
from pprint import pprint

SHEETY_BEARER_TOKEN = environ["SHEETY_BEARER_TOKEN"]


sheety_header = {
    'Authorization': f"Bearer {SHEETY_BEARER_TOKEN}",
    "Content-type": "application/json"
}

get_sheety_header = {
    'Authorization': f"Bearer {SHEETY_BEARER_TOKEN}",
}

row_number = 0


class DataManagerV3:
    """This class is responsible for talking to the Google Sheet."""

    # TODO First time app run
    def __init__(self, sheet_name):
        self.sheet_name = sheet_name

        self.get_sheety_endpoint = "https://api.sheety.co/8d71f9dad050e97aca87b3b97e94d5d9" \
                                   "/pythonProgrammingGoogleSheetsApi/" \
                                   f"{self.sheet_name}"
        self.post_sheety_endpoint = "https://api.sheety.co/8d71f9dad050e97aca87b3b97e94d5d9" \
                                    "/pythonProgrammingGoogleSheetsApi/" \
                                    f"{self.sheet_name}"
        self.put_sheety_endpoint = "https://api.sheety.co/8d71f9dad050e97aca87b3b97e94d5d9" \
                                   "/pythonProgrammingGoogleSheetsApi/" \
                                   f"{self.sheet_name}/{row_number}"
        self.delete_sheety_endpoint = "https://api.sheety.co/8d71f9dad050e97aca87b3b97e94d5d9" \
                                      "/pythonProgrammingGoogleSheetsApi/" \
                                      f"{self.sheet_name}/{row_number}"

        self.first_run()

    def first_run(self):
        # TODO Create directory if it doesn't exist
        if not path.exists("data"):
            mkdir("data")
        # TODO Check for any data from the Google sheets and if it exists add it to the treeview and local csv file
        if not path.exists("data/saved searches.csv"):
            # TODO Check number of rows in the Google sheet
            search_params_dict = self.get_sheet_data()
            if len(search_params_dict) != 0:
                # TODO Add the data to a CSV file
                # search_params_dataframe = pandas.DataFrame(search_params_dict, index=[0])
                search_params_dataframe = pandas.DataFrame(search_params_dict)
                search_params_dataframe.to_csv("data/saved searches.csv", index=False, header=True)

    # TODO Get data from Google sheets using sheety
    def get_sheet_data(self):
        response = requests.get(self.get_sheety_endpoint, headers=get_sheety_header)
        response.raise_for_status()
        sheet_data = response.json()
        # print(sheet_data)
        # pprint(sheet_data)

        # TODO Save the sheety data in a local json file
        # with open("data/sheety data.json", mode="w") as json_file:
        #     json.dump(sheet_data, json_file, indent=4)

        # TODO Get the sheet data only
        sheet_data = sheet_data[self.sheet_name]
        # print(sheet_data_list)

        return sheet_data

    def save_search(self, search_params: dict):
        """
        This method saves the search parameters locally in csv file and online in a Google sheet
        :param search_params: A dict of search parameters to be saved
        """
        # TODO Save the data in a CSV file

        header_status = True
        if path.exists("data/saved searches.csv"):
            header_status = False
        search_params_dataframe = pandas.DataFrame(search_params, index=[0])
        print(search_params)
        print(search_params_dataframe)
        search_params_dataframe.to_csv("data/saved searches.csv", mode="a", index=False, header=header_status)

        # TODO Upload the data to the Google sheet
        row_data = {
            self.sheet_name: search_params
        }

        response = requests.post(
            self.post_sheety_endpoint,
            json=row_data,
            headers=sheety_header)
        response.raise_for_status()

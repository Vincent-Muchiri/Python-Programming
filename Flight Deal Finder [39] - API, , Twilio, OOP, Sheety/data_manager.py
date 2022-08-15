import requests
import os


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

class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    # TODO Get data from Google sheets using sheety
    def get_sheet_data(self, sheet_name: str):
        response = requests.get(get_sheety_endpoint, headers=sheety_header)
        response.raise_for_status()
        sheet_data = response.json()
        # print(sheet_data)
        # pprint(sheet_data)

        # TODO Save the sheety data in a local json file
        # with open("data/sheety data.json", mode="w") as json_file:
        #     json.dump(sheet_data, json_file, indent=4)

        # TODO Get the sheet data only
        sheet_data = sheet_data[sheet_name]
        # print(sheet_data_list)

        return sheet_data
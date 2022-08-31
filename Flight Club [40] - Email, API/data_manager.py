import requests
from os import path, mkdir, environ
import pandas
from tkinter import messagebox

# SHEETY_BEARER_TOKEN = environ["SHEETY_BEARER_TOKEN"]


sheety_header = {
    # 'Authorization': f"Bearer {SHEETY_BEARER_TOKEN}"
    "Content-type": "application/json"
}

row_number = 0


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    # TODO First time app run
    def __init__(self, sheet_name):
        self.get_sheety_endpoint = "https://api.sheety.co/8d71f9dad050e97aca87b3b97e94d5d9/flightClubLesson40/" \
                                   f"{sheet_name}"
        self.post_sheety_endpoint = "https://api.sheety.co/8d71f9dad050e97aca87b3b97e94d5d9/flightClubLesson40/" \
                                    f"{sheet_name}"
        self.put_sheety_endpoint = "https://api.sheety.co/8d71f9dad050e97aca87b3b97e94d5d9/flightClubLesson40/" \
                                   f"{sheet_name}/{row_number}"
        self.delete_sheety_endpoint = "https://api.sheety.co/8d71f9dad050e97aca87b3b97e94d5d9/flightClubLesson40/" \
                                      f"{sheet_name}/{row_number}"

        self.sheet_name = sheet_name

        self.first_run(sheet_name)

    def first_run(self, sheet_name: str):
        pass

    # TODO Get data from Google sheets using sheety
    def get_sheet_data(self):
        response = requests.get(self.get_sheety_endpoint, headers=sheety_header)
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
        :param sheet_name: Name of the Google sheet to save data to
        :param search_params: A dict of search parameters to be saved
        """
        # TODO Save the data in a CSV file
        search_params_dataframe = pandas.DataFrame(search_params, index=[0])
        header_status = True
        if path.exists("data/saved searches.csv"):
            header_status = False

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
        print(response.text)
        print(response.raise_for_status())

    def login_process(self, login_info: dict):
        """
        This method handles the login process
        :param login_info: Get the user login info
        :return: Returns True if the user wants to change the email. Default value is False
        """
        return_value = False

        # TODO Get the sheet data
        sheet_data = self.get_sheet_data()
        user_email = login_info["email"]

        if not any(d['email'] == user_email for d in sheet_data):  # IF the email doesn't exist, add the data
            # TODO Upload the data as a row
            row_name = self.sheet_name.removesuffix("s")  # The row name is the singular form of sheet name
            response = requests.post(
                self.post_sheety_endpoint,
                headers=sheety_header,
                json={row_name: login_info}  # Data must be nested in a key similar to row name
            )
            response.raise_for_status()
            if response.status_code == 200:
                messagebox.showinfo(message=f"{login_info['firstName']} {login_info['lastName']} has been saved "
                                            f"successfully!")

        else:
            reply = messagebox.askyesno(title="Signing you up",
                                        message="The email you are trying to enter "
                                                "is already in use!\n"
                                                "Would you like to try another email address?")

            if reply:
                return_value = True

        return return_value

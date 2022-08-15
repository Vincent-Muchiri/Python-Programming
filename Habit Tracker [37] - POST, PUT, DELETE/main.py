import requests
import os
from datetime import datetime

# --------------------------------------------- VARIABLES AND CONSTANTS ------------------------------------------------
# username = os.environ['pixela_username']
graph_id = ""
# graph_id = "graph"

TOKEN = os.environ['pixela_token']
HEADER = {
    'X-USER-TOKEN': TOKEN
}


# ------------------------------------------------- FUNCTIONS ----------------------------------------------------------
def date_format():
    # TODO Get the current date
    choice_date = datetime.now().date()

    # TODO Get the date from the calendar widget

    # TODO Convert the datetime module to a string
    choice_date_str = choice_date.strftime("%Y%m%d")
    return choice_date_str


# TODO Create new username
def create_username():
    global username, TOKEN
    pixela_endpoint = "https://pixe.la/v1/users"

    username_params = {}
    username_params = {
        'token': TOKEN,
        'username': username,
        'agreeTermsOfService': "yes",
        'notMinor': "yes"
    }

    response = requests.post(url=pixela_endpoint, json=username_params)
    # response.raise_for_status()
    print(response.text)


def create_graph():
    global graph_id, username
    # TODO Prompt user to create a new graph

    graph_params = {
        'id': graph_id,
        'name': "Cycling Graph",
        'unit': "Km",
        'type': "float",
        'color': "shibafu",
    }

    pixela_graph_endpoint = f"https://pixe.la/v1/users/{username}/graphs"
    response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=HEADER)
    response.raise_for_status()
    print(response.text)


def post_pixel():
    # TODO Post a pixel
    pixela_pixel_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}"

    pixel_params = {
        'date': date_format(),
        'quantity': "8.3"  # Type string
    }

    response = requests.post(url=pixela_pixel_endpoint, json=pixel_params, headers=HEADER)
    response.raise_for_status()
    print(response.text)
    # https://pixe.la/v1/users/vincent2/graphs/graph.html


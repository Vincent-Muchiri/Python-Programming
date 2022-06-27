import requests
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

USERNAME = os.environ['pixela_username']
TOKEN = os.environ['pixela_token']

pixela_endpoint = "https://pixe.la/v1/users"

pixela_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': "yes",
    'notMinor': "yes"
}

# TODO Create endpoint
# response = requests.post(url=pixela_endpoint, json=pixela_params)

# TODO Create a graph
GRAPHID = "graph"
graph_params = {
    'id': GRAPHID,
    'name': "Cycling Graph",
    'unit': "Km",
    'type': "float",
    'color': "shibafu",
}

headers = {
    'X-USER-TOKEN': TOKEN
}

pixela_graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

# response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=headers)

# TODO Post a pixel
pixela_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}"

# TODO Get the current date
today_dt = datetime.now().date()

# TODO Convert the datetime module to a string
today_str = today_dt.strftime("%Y%m%d")

pixel_params = {
    'date': today_str,
    'quantity': "8.3"  # Type string
}

# response = requests.post(url=pixela_pixel_endpoint, json=pixel_params, headers=headers)
# https://pixe.la/v1/users/vincent2/graphs/graph.html

# TODO Updating an already existing pixel using PUT request
date_str = today_str
pixela_put_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/{date_str}"
put_params = {
    'quantity': "9.0",
}
# response = requests.put(url=pixela_put_endpoint, json=put_params, headers=headers)

# TODO Delete an entry
pixela_delete_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/{date_str}"
response = requests.delete(url=pixela_delete_endpoint, headers=headers)
response.raise_for_status()
print(response.text)

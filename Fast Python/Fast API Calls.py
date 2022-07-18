import requests
from time import time
from datetime import timedelta
import json
import aiohttp
import asyncio
import threading

league_id_list = ["DNK", "ISL", "SEN", "EGY", "URY", 'GMB', 'ITA', "ITL", "DZA", "ARG", "AUS", "PRY", "SGP", "NOR",
                  "BRA", "ALB", "PER", "HUN", "FIN", "LTU", "SWE", "CHL", "JAM", "USA", "IRN", "COL"]


def odibet_api_call(league_id):
    odibet_today_league_soccer_json_list = []
    endpoint_url = f"https://apis.odibets.com/v4/matches?"
    params = {
        'src': 2,
        'sport_id': "soccer",
        'tab': "today",
        'trials': "0"
    }
    payload = {}
    headers = {}

    # TODO Assign the league string to the dict
    params['country_id'] = league_id

    # TODO Call the API
    response = requests.request("GET", endpoint_url, params=params, headers=headers, data=payload)
    response.raise_for_status()

    # print(len(response.json()['data']['competitions']))

    # TODO Check whether there's a game played in the league
    if len(response.json()['data']['competitions']) != 0:
        # TODO Save data in JSON format
        odibet_today_league_soccer_json_list.append(response.json())


# --------------------------------------------- Normal http requests Calls ---------------------------------------------
def using_request():
    # TODO Calculate the time taken
    start_time = time()

    # TODO Loop through the list of league ids
    for league in league_id_list:
        odibet_api_call(league_id=league)

    # TODO Print the time taken
    duration = timedelta(seconds=time() - start_time)

    print(f"It took {duration} to run make API calls using normal requests")
using_request()


# -------------------------------------------------- Using sessions ----------------------------------------------------
def using_sessions():
    start_time = time()

    with requests.Session() as session:
        for league in league_id_list:
            odibet_api_call(league_id=league)
    duration = timedelta(seconds=time() - start_time)

    print(f"It took {duration} to make API calls using sessions")
using_sessions()


# ---------------------------------------------------- aiohttp ---------------------------------------------------------



# -------------------------------------- aiohttp with concurrency(task switching) --------------------------------------



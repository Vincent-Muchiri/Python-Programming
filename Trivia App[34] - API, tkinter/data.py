import requests
import os
import json
from datetime import datetime
import html

path = ""

parameters = {
    "amount": 10,
    "type": "boolean"
}

trivia_ques_list = []

# https://opentdb.com/api.php?amount=10&type=boolean

# TODO Get data from the API
# response = requests.get(url="https://opentdb.com/api.php", params=parameters)
#
# # TODO Raise any exceptions
# response.raise_for_status()
#
# # TODO Store that data in a variable in JSON format
# raw_json_data = response.json()
#
# # TODO Extract only the questions and answers
# trivia_json_data = raw_json_data['results']

# TODO Create a directory/folder to store the data
# Using try to catch exception if folder exists
try:
    path = "./data_files"
    os.mkdir(path)
except FileExistsError:
    pass

# Using if to check whether folder already exists
# if not os.path.exists(path):
#     os.makedirs(path)

# TODO Get today's date
current_date = datetime.now().date()

# TODO Add json data to the directory on a daily basis i.e different questions different day
# with open(f"{path}/{current_date}_trivia_data.json", mode="w") as trivia_file:
#     json.dump(trivia_json_data, trivia_file, indent=4)

# TODO Offline testing
with open(f"{path}/2022-06-09_trivia_data.json", mode="r") as trivia_file:
# with open(f"{path}/{current_date}_trivia_data.json", mode="r") as trivia_file:
    trivia_json_data = json.load(trivia_file)

# TODO Create a list of dictionaries with question and answer pair
for elem_dict in trivia_json_data:
    # TODO Format the data and add it to the dictionary
    # question = elem_dict['question']
    # question = question.replace("&quot;", "'")
    # question = question.replace("&#039;", "'")

    # TODO Unescape HTML entities
    question = html.unescape(elem_dict['question'])

    answer = elem_dict['correct_answer']

    trivia_ques_dict = {'question': question, 'answer': answer}

    # TODO Append the dicts to a list
    trivia_ques_list.append(trivia_ques_dict)


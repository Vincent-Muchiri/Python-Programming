from datetime import datetime

exercise_dict = {'exercises': [{'tag_id': 317, 'user_input': 'ran', 'duration_min': 30, 'met': 9.8, 'nf_calories': 364.56, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None}, {'tag_id': 63, 'user_input': 'swam', 'duration_min': 30, 'met': 6, 'nf_calories': 223.2, 'photo': {'highres': None, 'thumb': None, 'is_user_uploaded': False}, 'compendium_code': 18310, 'name': 'swimming', 'description': None, 'benefits': None}]}

sheet_name = "sheet1"

date_obj = datetime.now().date()
date_str = date_obj.strftime("%d/%m/%Y")
time_obj = datetime.now().time()
time_str = time_obj.strftime("%H:%M:%S")

print(date_str, time_str)

cleaned_workout_dict = {
}
rows_list = []

exercise_list = exercise_dict["exercises"]

# TODO Append dicts in the list
for workout in exercise_list:
    row = {}
    row['date'] = date_str
    row['time'] = time_str
    row['exercise'] = workout['user_input']
    row['duration'] = workout['duration_min']
    row['calories'] = workout['nf_calories']

    # TODO Append the dict to the list
    rows_list.append(row)

# TODO Add the rows in the dict
cleaned_workout_dict[sheet_name] = rows_list
print(cleaned_workout_dict)

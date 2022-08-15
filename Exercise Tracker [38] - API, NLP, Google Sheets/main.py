import requests
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from datetime import datetime
from pprint import pprint
import os

# TODO Environmental variables
NUTRITIONIX_API_KEY = os.environ["NUTRITIONIX_API_KEY"]
NUTRITIONIX_APP_ID = os.environ["NUTRITIONIX_APP_ID"]
SHEETY_API_KEY = os.environ["SHEETY_API_KEY"]
SHEETY_BEARER_TOKEN = os.environ["SHEETY_BEARER_TOKEN"]

exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_headers = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY
}
sheety_header = {
    'Authorization': f"Bearer {SHEETY_BEARER_TOKEN}"
}

sheety_get_endpoint = f"https://api.sheety.co/{SHEETY_API_KEY}/pythonProgrammingGoogleSheetsApi/workoutTrackerDay38"
sheety_post_endpoint = f"https://api.sheety.co/{SHEETY_API_KEY}/pythonProgrammingGoogleSheetsApi/workoutTrackerDay38"
sheety_put_endpoint = f"https://api.sheety.co/{SHEETY_API_KEY}/pythonProgrammingGoogleSheetsApi/workoutTrackerDay38/[Object ID]"
sheety_delete_endpoint = f"https://api.sheety.co/{SHEETY_API_KEY}/pythonProgrammingGoogleSheetsApi/workoutTrackerDay38/[Object ID]"


# --------------------------------------------------- Functions --------------------------------------------------------
# TODO Test Get
# test_get_response = requests.get(sheety_get_endpoint)
# test_get_response.raise_for_status()
# sheet_data = test_get_response.json()
# pprint(sheet_data)

# TODO Test Put
test_dict = {'workoutTrackerDay38': {'date': '18/07/2022', 'time': '05:52:10', 'exercise': 'Running', 'duration': 60, 'caloriesBurnt': 758.52}}
test_dict2 = {'workoutTrackerDay38': [{'date': '18/07/2022', 'time': '13:05:59', 'exercise': 'Running', 'duration': 60, 'caloriesBurnt': 725.2}, {'date': '18/07/2022', 'time': '13:05:59', 'exercise': 'Swimming', 'duration': 20, 'caloriesBurnt': 148}]}
#
# response = requests.post(url=sheety_post_endpoint, json=test_dict2)
# response.raise_for_status()
# print(response.text)


# TODO Change strings to camel case
def camel_case_changer(original_str):
    final_str = ""

    strings_list = original_str.split(" ")
    for string in strings_list:
        if strings_list.index(string) == 0:
            final_str = string.lower()
        else:
            final_str += string.title()

    return final_str


def upload_workout_window(exercise_dict):
    # --------------------------------------------------- Functions ----------------------------------------------------
    # TODO Get the current date and time as strings
    date_obj = datetime.now().date()
    date_str = date_obj.strftime("%d/%m/%Y")
    time_obj = datetime.now().time()
    time_str = time_obj.strftime("%H:%M:%S")

    def upload_workout():
        # TODO Get entry values and convert sheet name to camel case
        sheet_name = camel_case_changer(sheetname_entry.get())
        date = date_entry.get()
        time = time_entry.get()

        # TODO Initialise dicts and lists
        sheet_data_dict = {}
        exercise_list = exercise_dict["exercises"]

        # TODO Append dicts in the list
        for workout in exercise_list:
            row = {}
            row['date'] = date_str
            row['time'] = time_str
            row['exercise'] = workout['name'].title()
            row['duration'] = workout['duration_min']
            row['caloriesBurnt'] = workout['nf_calories']

            sheet_data_dict[sheet_name] = row
            # print(sheet_data_dict)

            # TODO Call API
            try:
                response = requests.post(url=sheety_post_endpoint, json=sheet_data_dict, headers=sheety_header)
            except:
                messagebox.showerror(message=response.text)
            else:
                # print("Sheety API works")
                pass

        messagebox.showinfo(message="Workout data uploaded successfully to Google Sheets")

        # TODO Clear the entries
        # date_entry.delete(0, END)
        # time_entry.delete(0, END)
        # sheetname_entry.delete(0, END)

        # TODO Delete all the entries
        query_text.delete("1.0", END)
        gender_radio_state.set(value="")
        weight_entry.delete(0, END)
        height_entry.delete(0, END)
        age_entry.delete(0, END)

        # TODO Close toplevel
        upload_workout_toplevel.destroy()

    # ----------------------------------------------------- UI ---------------------------------------------------------
    upload_workout_toplevel = Toplevel()
    upload_workout_toplevel.transient(window)
    upload_workout_toplevel.title("Upload Workout To Google Sheets")
    upload_workout_toplevel.iconphoto(False, app_icon)
    upload_workout_toplevel.geometry("330x250")
    upload_workout_toplevel.minsize(width=330, height=250)
    upload_workout_toplevel.config(padx=20, pady=10)
    upload_workout_toplevel.grab_set()

    # TODO Date
    date_frame = ttk.Frame(upload_workout_toplevel)
    date_frame.pack()

    date_label = ttk.Label(date_frame, text="Date (dd/mm/yyyy):")
    date_label.grid(row=0, column=0)

    date_entry = ttk.Entry(date_frame)
    date_entry.insert(0, date_str)
    date_entry.grid(row=0, column=1, padx=20)

    # TODO Time
    time_frame = ttk.Frame(upload_workout_toplevel)
    time_frame.pack()

    time_label = ttk.Label(time_frame, text="Time (hh:mm:ss):")
    time_label.grid(row=0, column=0)

    time_entry = ttk.Entry(time_frame)
    time_entry.insert(0, time_str)
    time_entry.grid(row=0, column=1, padx=20, pady=20)

    # TODO Sheet
    sheetname_frame = ttk.Frame(upload_workout_toplevel)
    sheetname_frame.pack()

    sheetname_label = ttk.Label(sheetname_frame, text="Sheet Name:")
    sheetname_label.grid(row=0, column=0)

    sheetname_entry = ttk.Entry(sheetname_frame)
    sheetname_entry.insert(0, "Workout Tracker Day 38")
    sheetname_entry.grid(row=0, column=1, padx=20)

    # TODO Upload button
    upload_btn = ttk.Button(upload_workout_toplevel, text="Upload Workout", style="Accentbutton", command=upload_workout)
    upload_btn.config(width=30)
    upload_btn.pack(pady=20)


def process_workout_data():
    # TODO Check whether fields are empty
    if query_text.get("1.0", END) == "\n":
        messagebox.showerror(message="Please enter a query")
        query_text.focus()
    elif weight_entry.get() == "":
        weight_entry.state(["invalid"])
        messagebox.showerror(message="Please enter the weight")
        weight_entry.focus()
    elif height_entry.get() == "":
        height_entry.state(["invalid"])
        messagebox.showerror(message="Please enter the height")
        height_entry.focus()
    elif age_entry.get() == "":
        age_entry.state(["invalid"])
        messagebox.showerror(message="Please enter the age")
        age_entry.focus()
    elif gender_radio_state.get() == "":
        messagebox.showerror(message="Select a gender")
    else:
        # TODO Get all the data
        query = query_text.get("1.0", END)
        gender = gender_radio_state.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())

        # TODO Assert the values
        assert weight > 0, messagebox.showerror(message="The weight should be greater then zero")
        assert height > 0, messagebox.showerror(message="The height should be greater then zero")
        assert age > 0, messagebox.showerror(message="The age should be greater then zero")

        # TODO Remove the "\n" from the query string
        query = query.strip("\n")

        # TODO Create the params dictionary
        params = {
            'query': query,
            'gender': gender,
            'weight_kg': weight,
            'height_cm': height,
            'age': age
        }

        # TODO Call the API
        try:
            response = requests.post(url=exercise_url, json=params, headers=exercise_headers)
        except:
            messagebox.showerror(message=response.text)
        else:
            # print(response.json())
            workout_json = response.json()

            # TODO Prompt the user to upload data to Google sheets
            answer = messagebox.askyesno(message="Data processed successfully.\n"
                                                 "Do you wish to save the workout in Google Sheets?")

            if answer:
                # TODO Open a pop up window
                upload_workout_window(exercise_dict=workout_json)


# ------------------------------------------------------- UI -----------------------------------------------------------
# TODO Configure the window
window = Tk()
window.geometry("300x400")
window.title("Nutritionix Exercise Tracker")
window.config(padx=20, pady=20)

app_icon = PhotoImage(file="images/calendar_dark_512.png")
window.iconphoto(False, app_icon)

# TODO Set window styling
style = ttk.Style(window)
window.tk.call('source',
               'C:/Users/Vin Muchiri/OneDrive/Python Programming/_packages/Azure-ttk-theme-main/azure/azure.tcl')
style.theme_use('azure')
style.configure("Accentbutton", foreground="white")

# TODO Query text entry
query_text = Text(height=5, width=35)
query_text.focus()
query_text.pack()

# TODO Gender radio buttons
gender_labelframe = ttk.LabelFrame(text="Choose a gender")
gender_labelframe.config(padding=10)
gender_labelframe.pack(fill="both")

gender_radio_state = StringVar()
male_radiobtn = ttk.Radiobutton(gender_labelframe, text="Male", value="male", variable=gender_radio_state)
female_radiobtn = ttk.Radiobutton(gender_labelframe, text="Female", value="female", variable=gender_radio_state)
# male_radiobtn.pack(side="left")
# female_radiobtn.pack(side="right")
male_radiobtn.grid(row=0, column=0)
female_radiobtn.grid(row=0, column=1, padx=40)

# TODO General frame
general_frame = ttk.Frame()
general_frame.config()
general_frame.pack(pady=20)

# Weight
weight_label = ttk.Label(general_frame, text="Weight(kg):")
weight_label.grid(row=0, column=0, padx=20)

weight_entry = ttk.Entry(general_frame)
weight_entry.grid(row=0, column=1)

# Height
height_label = ttk.Label(general_frame, text="Height(cm):")
height_label.grid(row=1, column=0, padx=20, pady=20)

height_entry = ttk.Entry(general_frame)
height_entry.grid(row=1, column=1)

# Age
age_label = ttk.Label(general_frame, text="Age(years):")
age_label.grid(row=2, column=0, padx=20)

age_entry = ttk.Entry(general_frame)
age_entry.grid(row=2, column=1)

# TODO Submit button
submit_btn = ttk.Button(text="Process Data", style="Accentbutton", command=process_workout_data)
submit_btn.config(width=20)
submit_btn.pack()

window.mainloop()





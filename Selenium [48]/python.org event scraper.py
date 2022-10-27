from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import pandas
from os import mkdir, path

# TODO Store the chrome drivers executable file path in a variable
chrome_exe_file = "../chromedriver.exe"

# TODO Instantiate the Chrome webdriver
chrome_driver = webdriver.Chrome(executable_path=chrome_exe_file)

# TODO Open the webpage link
url = "https://www.python.org"
chrome_driver.get(url)

# TODO Get the dates and store them in a list
# event_dates = [event_date.text for event_date in chrome_driver.find_elements(By.CLASS_NAME, "say-no-more")]
event_dates = [event_date.get_attribute("datetime").split("T")[0] for event_date in chrome_driver.find_elements(By.CSS_SELECTOR, ".event-widget time")]
# print(event_dates)

# TODO Get the names and store them in a list
event_names = [event_name.text for event_name in chrome_driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')]
# print(event_names)

events_dict = {}
# TODO Make a dictionary and append it
for index in range(len(event_names)):
    events_dict[index] = {
        "Time": event_dates[index],
        "Name": event_names[index]
    }
# print(events_dict)

# TODO Check if the folder exists
data_dir = "data"
if not path.exists("data"):
    mkdir("data")

# TODO Save the file in json file
with open("data/events.json", mode="w") as json_file:
    json.dump(events_dict, json_file, indent=4)

# TODO Save the data in a CSV file
csv_events_dict = {
    "Event Name": event_names,
    "Event Date": event_dates
}
events_dataframe = pandas.DataFrame(csv_events_dict)
events_dataframe.to_csv("data/events.csv")

# TODO Close the window
chrome_driver.quit()

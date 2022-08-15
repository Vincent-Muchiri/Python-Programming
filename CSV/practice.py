# TODO Using CSV library print the dataframe and a list of temperature values as integers
# TODO Use pandas to generate a dataframe
# TODO Using pandas extract the temperature column and store it in a list
# TODO Convert dictionary to dataframe
# TODO Store a dataframe into a CSV file
# TODO Open the csv file created above

# Using CSV to print a list of temperature values as integers
import csv

# with open("weather_data.csv") as weather_file:
#     weather_data = csv.reader(weather_file)
#     print(weather_data)
#     # Print the dataframe
#     for row in weather_data:
#         print(row)
#     # Print an int list of temperatures
#     temp_list = []
#     for temp_row in weather_data:
#         # print(row[1])
#         if temp_row[1] != "temp":
#             temp_list.append(int(temp_row[1]))
#     print(temp_list)

import pandas

weather_data = pandas.read_csv("weather_data.csv")
# print(weather_data)
temp_list = weather_data.temp.to_list()
# print(temp_list)
temp_list2 = weather_data["temp"].to_list()
# print(temp_list2)

performance_dict = {
    "Student Name": ["Vincent", "Diana", "Mark"],
    "Marks": [89, 90, 87]
}

performance_dataframe = pandas.DataFrame(performance_dict)
# print(performance_dataframe)

# Store dataframe inside a CSV
performance_dataframe.to_csv("student_data.csv")

# Open the created csv
student_data = pandas.read_csv("student_data.csv")
print(student_data)

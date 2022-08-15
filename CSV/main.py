# with open("./weather_data.csv", "r") as weather_file:
#     data = weather_file.readlines()
#     print(data)

# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     temperatures = []
#     for row in data:
#         # print(row)
#         temp = row[1]
#         # print(temp)
#         if temp != 'temp':
#             temp = int(temp)
#             temperatures.append(temp)
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)

# Converting a dataframe into a dictionary
# print(data.to_dict())

# Converting the temp series(column) to a list
temp_list = data["temp"].to_list()
temp_list = data.temp.to_list()
# print(temp_list)

# Calculating the average temperature
sum_temp = 0
for temp in temp_list:
    sum_temp += temp

# sum_temp = sum(temp_list)
avg_temp = sum_temp / len(temp_list)
# print(avg_temp)
mean_temp = data["temp"].mean()
# print(mean_temp)

# Find the maximum temperature
max_temp = data.temp.max()
# print(max_temp)

# Getting hold of the rows
# print(data[data.day == "Monday"])

# Getting the day, temp and condition of the hottest day of the week
# print(data[data.temp == data.temp.max()])

# Get Mondays temp and convert it to fahrenheit
monday = data[data.day == "Monday"]
# print(monday)
temp_celcius = monday.temp
# print(temp_celcius)
temp_fahrenheit = temp_celcius * 9 / 5 + 32
# print(temp_fahrenheit)

# Creating data frame from scratch
data_dict = {
    "student": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
# print(data)
# Saving the dataframe into a csv file
data.to_csv("new_data.csv")

# TODO Looping through a dataframe
student_dataframe = pandas.read_csv("new_data.csv")
# TODO Printing the columns of the data - not useful
for (index, value) in student_dataframe.items():
    # print(index)
    # print(value)
    pass

# TODO Print the row of the dataframe
for (index, row) in student_dataframe.iterrows():
    print(row)
    # Print the names only
    print(row.student)
    # TODO Print a specific value
    if row.student == "Amy":
        print(row.score)


# # TODO Ways to orient a dataframe
# # TODO Add data to CSV without overwriting the previous data
# # Read the csv file if any
# csv_file_data = pandas.read_csv("test.csv")
# print(csv_file_data)
#
# # Convert the dataframe to a dict
# for orient in ["dict", "list", "series", "split", "records", "index"]:
#     csv_data_dict = csv_file_data.to_dict(orient=orient)
#     print(orient)
#     print(csv_data_dict)
#     print("")

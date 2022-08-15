import pandas
# TODO Looping through a dataframe
student_dataframe = pandas.read_csv("../CSV/new_data.csv")
# TODO Printing the columns of the data - not useful
for (index, value) in student_dataframe.items():
    # print(index)
    # print(value)
    pass

# TODO Print the row of the dataframe
for (index, row) in student_dataframe.iterrows():
    # print(row)
    # Print the names only
    # print(row.student)
    # TODO Print a specific value
    if row.student == "Amy":
        print(row.score)

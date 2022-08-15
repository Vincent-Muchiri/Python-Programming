import pandas
# TODO Errors

# TypeError
num = 1
string = "a"
# total = num + string

# TODO Syntax error
# for i in range(2) while:
#     print(i)

# if num = 1:
#     print(string)

# TODO KeyError
some_dict = {
    "key1": 1,
    "key2": 2
}
# print(some_dict["key3"])

# TODO IndexError
some_list = [0, "one", 2]
# print(some_list[4])

# TODO FileNotFound
# data = pandas.read_csv("missing file.csv")

# with open("missing file.txt", mode="r") as missing_file:
#     data = missing_file.read()

# TODO Exceptions
from tkinter import messagebox
try:
    file_name = "some_file.txt"
    file = open(file_name)

    some_list = [0, "one", 2]
    print(some_list[0])
except FileNotFoundError:
    create_file = messagebox.askyesno(title="Missing File", message=f"{file_name} does not exist. Do you want to create it?")
    if create_file:
        file = open(file_name, mode="w")
        file.write("Something")
        print(f"{file_name} created successfully!")
except IndexError as error_message:
    print(f" The index {error_message} doesn't exist")
else:
    contents = file.read()
    print(contents)
finally:
    file.close()
    print("File was closed")
# TODO Create an exception
    raise KeyError("This is an error I made up.")


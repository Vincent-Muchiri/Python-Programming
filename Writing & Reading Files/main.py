# file = open
# contents = file.read()
# print(contents)
# file.close()
with open("my_file.txt", mode="w") as file: # Overwrites the original content
    file.write("My name is Vincent Muchiri")

with open("my_file.txt") as file: # Reads the content
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="a") as file: # Appends new content
    file.write(" I'm an award-winning talented programmer, engineer and serial entrepreneur.")
    print(contents)

with open("my_file.txt", mode="r") as file: # Opens the file in read mode
    print(file.read())

# TODO Using ABSOLUTE file path to access an existing file named "types of file paths.txt"
with open("C:/Users/Vin Muchiri/OneDrive/Documents/Python Programming/txt files/types of file paths.txt", mode="r") as \
        file:
    contents = file.read()
    print(contents)

# TODO Using RELATIVE file path write onto the above file
with open("../txt files/types of file paths.txt", mode="a") as file:
    file.write("\nRelative file path\n")
    file.write("This file can be read and written by ../Writing & Reading Files/python sequences.py\n")

# TODO Using RELATIVE file path print the contents of "types of file paths.txt"
with open("../txt files/types of file paths.txt", mode="r") as file:
    print(file.read())

from os import mkdir, path, makedirs

# --------------------------------------------- mkdir ------------------------------------------------
# mkdir is used to make a single folder
# TODO Create a new none existing folder
directory = "./mkdir_folder"

try:
    mkdir(directory)

# TODO Check whether a directory exists using exceptions
except FileExistsError:
    print("Folder already exists!")

# TODO Check whether a directory exists using if statements and exists method
directory_2 = "./mkdir_folder2"
if not path.exists(directory_2):
    mkdir(directory_2)
else:
    print("Folder already exists!")

# --------------------------------------------- makedirs ------------------------------------------------
# makedirs allows you to create several nested folders
directory_3 = "./mkdir_folder/makedirs_folder1/makedirs_folder2/makedirs_folder3"
if not path.exists(directory_3):
    makedirs(directory_3)
else:
    print("Folder already exists!")

# TODO Create a file in a nested directory
directory_4 = "./mkdir_folder/makedirs_folder1/makedirs_folder2/makedirs_folder3"
try:
    makedirs(directory_4)
except FileExistsError:
    import json
    with open(f"{directory_4}/new_file.json", mode='w') as file:
        json.dump("File created successfully", file)

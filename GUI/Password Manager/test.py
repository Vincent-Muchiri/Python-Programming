import json

data_dict = {
    "Amazon": {
        "Password": "asdas32y74yr2fh2o3",
        "Email": "vincentmuchiri1@gmail.com"
    }
}

test_dict = {
    "Status": "Successful"
}
# # TODO Create a json file
# with open("test.json", "w") as test_file:
#     json.dump(data_dict, test_file, indent=4)

# try:
#     # TODO Add data to the json file
#     with open("test.json", "r") as test_file:
#         data = json.load(test_file)
#         print(data)
# except FileNotFoundError:
#     with open("test.json", "w"):
#         print("Expression found")
#         pass
# else:
#     with open("test.json", "w") as test_file:
#         data.update(test_dict)
#         json.dump(data, test_file, indent=4)
#         print("Ran successfully")

with open("data.json", "r") as json_file:
    data = json.load(json_file)
    print(data)
    # print(type(data))
    print(data["Amazon"])
    for key in data:
        print(key)
        # if key == "Amazon":
        #     print("Amazon exists")
        # if key == "a":
        #     print("a doesn't exist")

web_list = [website for website in data]
print(web_list)
if "Amazon" in web_list:
    print("Amazon is in the list")
programming_dictionary = {
    "Bug" : "An unexpected problem with software or hardware",
    "Function": "Self contained modules of code that accomplish a specific task",
    404: "A signal that the webpage does not exist"
}

#Retrieving items in a dictionary
# print(programming_dictionary[404])

#Adding items to a dictionary
programming_dictionary["Loop"] = "A sequence of instruction s that is continually repeated until a certain condition is reached"
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary[404] = "An error"

#Looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

for (key, value) in programming_dictionary.items():
    print(key)
    print(value)

#Create an empty dictionary
empty_dictionary = {}
programming_dictionary = {}



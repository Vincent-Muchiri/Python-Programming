programming_dictionary = {"Bug": "An unexpected problem with software or hardware",
                          "Function": "Self contained modules of code that accomplish a specific task", 404: "An error",
                          "Loop": "A sequence of instruction s that is continually repeated until a certain condition " \
                                  "is reached "}

# TODO Retrieving items in a dictionary
# print(programming_dictionary[404])

# TODO Getting the key and values of elements of a dict using indexes
first_key = list(programming_dictionary.keys())[0]
first_value = list(programming_dictionary.values())[0]
first_key_value_tuple = list(programming_dictionary.items())[0]

# print(first_key, first_value)
# print(first_key_value_tuple)

# TODO Adding items to a dictionary
# print(programming_dictionary)

# TODO Edit an item in a dictionary

# TODO Looping through a dictionary
for key in programming_dictionary:
    pass
    # print(key)
    # print(programming_dictionary[key])

for (key, value) in programming_dictionary.items():
    pass
    # print(key)
    # print(value)

# TODO Create an empty dictionary
empty_dictionary = {}
programming_dictionary = {}

dict_list = [{'Class': "Form 1 East",
              "Name": "Vincent",
              "Marks": 98},
             {'Class': "Form 2 North",
              "Name": "Diana",
              "Marks": 80},
             {'Class': "Form 4 West",
              "Name": "Mark",
              "Marks": 20},
             {'Class': "Form 2 East",
              "Name": "Sam",
              "Marks": 24},
             {'Class': "Form 3 South",
              "Name": "Leah",
              "Marks": 87},
             {'Class': "Form 1 East",
              "Name": "Paul",
              "Marks": 67}
             ]


# TODO Sort a list of dict based on one parameter
from operator import itemgetter

sort_by_class = sorted(dict_list, key=itemgetter('Class'))
print(sort_by_class)

# TODO Sort a list based on two parameters
sort_by_class_marks = sorted(dict_list, key=lambda student_dict: (student_dict['Class'], student_dict['Marks']))
print(sort_by_class_marks)

# TODO Sort in descending order
sort_by_class_marks = sorted(dict_list, key=lambda student_dict: (student_dict['Class'], student_dict['Marks']), reverse=True)
print(sort_by_class_marks)

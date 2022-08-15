# TODO Dictionary comprehension
# new_dictionary = {new_key:new_value for item in list}
# new_dictionary = {new_key:new_value for item in dict.items()}

# TODO Conditional dictionary comprehension
# new_dict = {new_key:new-value for (key, value) in dict.items() if test}
# new_dict = {what we want to generate for }

names_list = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]

# TODO Dictionary comprehension
import random
students_scores = {students: random.randint(0, 100) for students in names_list}
# print(students_scores)

# TODO Conditional dictionary comprehension
# new_dict = {new_key:new-value for (key, value) in dict.items( if test)}
passed_students_dict = {students: students_scores[students] for students in students_scores if students_scores[students]
                        >= 50}
passed_students_dict2 = {students: score for (students, score) in students_scores.items() if score >= 50}

# print(passed_students_dict2)
# print(passed_students_dict)

# TODO Make a dictionary called 'result' containing words of the sentence as the keys and the length of the words as
#  the values

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result1 = {}
result2 = {}

word_list = sentence.split()
# print(word_list)
for word in word_list:
    result1[f"{word}"] = len(word)
print(result1)

result2 = {word: len(word) for word in word_list}
result2 = {word: len(word) for word in sentence.split()}
print(result2)

# TODO Convert temperature values in a dictionary to Fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

weather_f = {days: weather_c[days] * 9 / 5 + 32 for days in weather_c}
print(weather_f)

weather_f2 = {day: temp_c * 9 / 5 + 32 for (day, temp_c) in weather_c.items()}
print(weather_f2)

# TODO Looping through a dataframe


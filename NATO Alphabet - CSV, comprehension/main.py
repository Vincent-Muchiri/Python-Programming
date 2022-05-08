# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

import pandas
from tkinter import messagebox


# TODO Get data from a CSV file
nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_alphabet_data)
# print(nato_alphabet_data.to_dict()) # This won't work

# TODO Convert the data from a Dataframe to a dictionary
# nato_alphabet_dict = {}
# for (index, row) in nato_alphabet_data.iterrows():
#     nato_alphabet_dict[f"{row.letter}"] = row.code
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_data.iterrows()}
# print(nato_alphabet_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

is_incorrect = True
while is_incorrect:
    word = input("Enter a word: ").upper()
    letters_list = list(word)

    # print(letters_list)
    # nato_word_list = [output for determinant in source if condition]
    try:
        nato_word_list = [nato_alphabet_dict[letter] for letter in letters_list]
    except KeyError:
        # messagebox.showerror(title="KeyError", message="Enter letters only")
        print("Enter letters only")
    else:
        print(nato_word_list)
        is_incorrect = False

# try:
#     nato_word_list2 = [nato_alphabet_dict[letter] for letter in word]
# except KeyError:
#     messagebox.showerror(title="KeyError", message="Enter letters only")
# else:
#     print(nato_word_list2)

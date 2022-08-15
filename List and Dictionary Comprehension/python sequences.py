# TODO Python sequence
# lists, turples, range and string

# TODO List comprehension
# new_list = [new_item for item in python sequence]
# new_item is how item will be manipulated

# TODO Conditional list comprehension
# new_list = [new_item for old_item in old_sequence if condition]

num_list = [1, 2, 3, 4, 5]
# new_item = n + 1
new_numbers = [n+1 for n in num_list]
print(new_numbers)

name = "Vincent"
letter_list = [letter for letter in name]
print(letter_list)

new_num_list = [num*2 for num in range(1, 5)]
print(new_num_list)

names_list = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]
short_names = [name for name in names_list if len(name) < 5]
print(short_names)

caps_names = [name.upper() for name in names_list if len(name) > 4]
print(caps_names)



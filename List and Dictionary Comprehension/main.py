numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# TODO Create a list of square numbers
squared_numbers = [num*num for num in numbers]
# print(squared_numbers)

# TODO Create a list of even numbers
result = [num for num in numbers if num % 2 == 0]
# print(result)

# TODO Make a list of common numbers in files 1 and 2
clean_file1_contents = []
with open("file1.txt", "r") as file1:
    raw_file1_contents = file1.readlines()
    # print(raw_file1_contents)
    for num in raw_file1_contents:
        num = int(num.strip())
        clean_file1_contents.append(num)
    # print(clean_file1_contents)

with open("file2.txt", "r") as file2:
    raw_file2_contents = file2.readlines()
    clean_file2_contents = []
    for num in raw_file2_contents:
        num = int(num.strip())
        clean_file2_contents.append(num)
    # print(clean_file2_contents)

new_list = []
# for num in clean_file1_contents:
#     if num in clean_file2_contents:
#         new_list.append(num)
#
# print(new_list)

new_list = [num for num in clean_file1_contents if num in clean_file2_contents]
# print(new_list)

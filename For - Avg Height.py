
student_heights = input("Enter a list of student heights: ").split()
# print(student_heights) #Prints a list of strings


#Convert the strings into integers and put them in a list as such
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights) #Prints a lust of intergers
#180 124 165 173 189 169 164
#avg = 166
#avg_height = sum(student_height) / len(student_height)

i = 0
num_students = 0
sum_height = 0
# for n in range(0, len(student_heights)):
#     i += 1
#     sum_height = student_heights[n] + sum_height
#     avg_height = sum_height / i
#     # print(i)
#     # print(sum_height)
#     # print(avg_height)

for height in student_heights:
    sum_height += height
    num_students += 1
    avg_height = sum_height / num_students

avg_height = round(avg_height)
print(f"The total height for {num_students} students is {sum_height} and their average height is {avg_height}")
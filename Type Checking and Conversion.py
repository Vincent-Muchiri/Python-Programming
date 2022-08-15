size = len(input("What is your name? \n"))
# print("Your name has " +size+ " charachter") Type error
# print(type(size)) Check type
 
string_size = str(size)
print("Your name has " +string_size + " characters")

two_digit_num = input("Enter a twi digit number \n")
print(type(two_digit_num))
print(int(two_digit_num[0]) + int(two_digit_num[1]))
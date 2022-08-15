import random


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ["0","1","2","3","4","5","6","7","8","9"]
symb = ['!','?','@','#','$','%','&','*','(',')','+',' ']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? "))
nr_numbers = int(input("How many numbers would you like? "))
nr_symbols = int(input("How many symbols? "))

# password = ["asdlkasdads"]
# password.insert(2, "1")
# print(password)

password = []
len_password  = nr_symbols + nr_letters + nr_numbers
# print(len_password)

#Using the shuffle function
# for char in range(0, nr_letters):
#     password.append(random.choice(letters))
# for char in range(0, nr_numbers):
#     password += random.choice(num)
# for char in range(0, nr_symbols):
#     password += random.choice(symb)

# random.shuffle(password)
# print([password])

for i in range(0, nr_letters):
    password.insert(        random.randint(0, len_password - 1)        ,       letters[random.randint(0, len(letters)-1)]                      )
    # print(password)
for j in range(0, nr_numbers):
    password.insert(        random.randint(0, len_password - 1)        ,       num[random.randint(0, len(num) - 1)]                            )
    # print(password)
for k in range(0, nr_symbols):
    password.insert(        random.randint(0, len_password - 1)        ,       symb[random.randint(0, len(symb) - 1)]                          )
    # print(password)

print(len(password))
# print(password)


str_pass = ""
for ind in password:
    str_pass = str_pass + str(ind)

print(str_pass)
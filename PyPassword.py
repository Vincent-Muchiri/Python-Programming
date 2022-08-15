import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ["0","1","2","3","4","5","6","7","8","9"]
symb = ['!','?','@','#','$','%','&','*','(',')','+',' ']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? "))
nr_numbers = int(input("How many numbers would you like? "))
nr_symbols = int(input("How many symbols? "))

# pass_len = nr_letters + nr_numbers + nr_symbols
# password = []
password = ""

for i in range(0, nr_letters):
    # rand_num = str(random.randint(0, 9))
    # print(rand_num)
    # print(type(rand_num))
    # password[i] = letters[random.randint(0, len(letters))]
    # password = password = rand_num

    # password = password + letters[random.randint(0, len(letters) - 1)]
    password += random.choice(letters)
    # print(password)
for n in range(0, nr_numbers):
    # password = password + num[random.randint(0, len(num) - 1)]
    password += random.choice(num)
    # print(password)
for m in range(0, nr_symbols):
    # password = password + symb[random.randint(0, len(symb) - 1)]
    password += random.choice(symb)
    # print(password)
    
print(password)
import random

names = input("Give me everyones name seperated by a comma: \n")
names = names.split(",") #Creates a list of inputs
# print(names)

payer = random.randint(0, len(names) - 1)
print(payer)
print("The person paying the bill is "+names[payer])
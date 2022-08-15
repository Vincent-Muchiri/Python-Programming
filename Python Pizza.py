print("Welcome to Python Pizza Deliveries")

size = input("What size of pizza do you want? S, M or L? ")
add_pepperoni = input("Do you want pepperoini with your pizza? Y or N? ")
cheese = input("Do you want extra cheese? Y or N? ")

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill = 25
else:
    print("Error! Check whether you selected the right entry.")

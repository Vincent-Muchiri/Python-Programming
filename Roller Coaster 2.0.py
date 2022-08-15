height = int(input("Enter your height: "))

if height < 120:
    print("You don't meet the height requirement.")
else:
    age = int(input("Enter your age: "))
    photo = input("Do you want a photo taken? Yes or No?: ")
    # print(type(ticket))
    if age < 12:
        total_charge = 5
        print("Your adult ticket is $5")
    elif age < 18:
        total_charge = 7
        print("Your adult ticket is $7")
    elif age >= 45 and age <= 55:
        total_charge =0
        print(f"Your ticket is free!")
    else:
        total_charge = 12
        print("Your adult ticket is $12")
    

if photo == "No":
    print(f"Your total charge is ${int(total_charge)}")
else:
    total_charge += 3
    print(f"Your total charge is ${int(total_charge)}")
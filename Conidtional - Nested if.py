height = int(input("Enter your height: "))

if height < 120:
    print("You'll have to be taller to ride this rollercoaster")
else:
    age = int(input("Enter your age: "))
    if age < 12:
        print("Ticket costs $5")
    elif age > 18:
        print("Ticket costs $12")
    else:
        print("Tocket costs $7")


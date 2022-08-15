year = int(input("Which year do you want to check: "))

if year < 1851:
    print("Enter a year later than 1851")
else:
    if year % 4 != 0:
        print(f"{year} is a common year")
    else:
        if year % 400 != 0:
            print(f"{year} is a common year")
        elif year % 100 == 0:
            print(f"{year} is a leap year")
# Time left untill 90 years
age = input("Enter your current age? ")

years_left = 90 - int(age)
days_left = int(years_left * 365)
weeks_left = int(years_left * 52)
months_left = int(years_left * 12)

print(f"You have {days_left} days left, {weeks_left} weeks left and {months_left} months left.")
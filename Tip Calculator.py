# Tip Calculator
print("Welcome to the tip calculator")
bill_amount = float(input("What was the total bill in dollars? "))
percentage_tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = float(input("How many people to split the bill? "))

ind_amount = round(bill_amount * (1 + percentage_tip / 100) / people, 2)
ind_amount = "{:.2f}".format(ind_amount) #Limits decimal places to 2

print(f"Each person shouldpay: ${ind_amount}")
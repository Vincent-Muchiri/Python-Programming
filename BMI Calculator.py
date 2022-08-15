weight = input("Enter your weight in kilograms: ")
height = input("Enter your height in meters: ")

BMI = round(float(weight) / float(height) ** 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are under weight")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you are normal weight")  
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are overweight")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese")
else:
    print(f"Your BMI is {BMI}, you are clinically obese")

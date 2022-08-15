# PEMDAS () ** * / + - 
# Exponents **
# BMI
weight  = 1
height  = 1
#weight = input("Enter you weight in kilograms: ") # The input is always a string
#height = input("Enter your height in meters: ")

bmi = float(weight) / float(height) ** 2 #The result of any division, including whole numbers, is always a float
print(round(bmi, 3))
print(round(bmi)) #Rounds up or down the figrue

int_bmi = float(weight) // float(height) ** 2 #Using two forward slashes converts the float into an int
print(int_bmi)
print(type(int_bmi))

score = 0
score += 1
#f-string removes the manual labour of converting data types
print(f"your score is {score}")

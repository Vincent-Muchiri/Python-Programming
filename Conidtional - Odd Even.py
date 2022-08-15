number = float

#Enter only integer
while type(number) is not int:
    number = int("Please enter an integer: ")

rem = number % 2

if number == 0:
    print("Zero")
elif rem == 0:
    print("Even")
else:
    print("Odd")

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

name1 = name1.lower()
name2 = name2.lower()

combined_name = name1 + name2

t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')
l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')

true = str(t+r+u+e)
love = str(l+o+v+e)

score = int(true + love)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}") 
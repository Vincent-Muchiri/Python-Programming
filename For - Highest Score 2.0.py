# 78 65 89 86 55 91 64 89

scores = input("Enter the scores in the class: ").split()

for i in range(0, len(scores)):
    scores[i] = int(scores[i])
# print(scores)

highscore = 0

for num in scores:
    if num > highscore:
        highscore = num
print(f"The highest score in class is: {highscore}")

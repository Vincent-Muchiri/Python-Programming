#78 65 89 86 55 91 64 89

scores = input("Enter a list of student scores: ").split()
# print(scores)

for i in range(0, len(scores)):
    scores[i] = int(scores[i])
# print(scores)



for num in scores:
    # rem = []
    n = 0
    m = 0
    sum_ones = 0
    # print(num)
    for divisor in scores:
        # print(f"The divisor is {divisor}")
        # print(scores[n])
        # print(scores[m])
        # rem = num % divisor
        # print(f"The remainder is: {rem}")
        if int(num / divisor) >= 1:
            ones = 1
        else:
            ones = 0
        # print(ones)
        sum_ones  = sum_ones + ones
    # print(sum_ones)
    # print("")
    if sum_ones == len(scores):
        print(f"The highest score in the class is: {num}")
        break
    
    



total = 0
for num in range(1, 12, 2):
    # print(num - 1)
    total = total + num - 1
print(total)

total = 0
for num in range(2, 11, 2):
    total += num
print(total)

total = 0
for num in range(1, 11):
    if num % 2 == 0:
        total += num
print(total)
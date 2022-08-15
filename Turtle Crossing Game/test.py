import random
some_list = [0, 2, 3, 4, 5]

new_list = []

for size in range(4):
    # TODO Add num
    new_list.append(random.randint(0,9))
    print(new_list)
    if len(new_list) == 1:
        pass
    else:
        for num in new_list:
            dif = num - new_list[-1]
            if dif >= 2:
                new_list[num] = random.randint(0, 9)

print(new_list)

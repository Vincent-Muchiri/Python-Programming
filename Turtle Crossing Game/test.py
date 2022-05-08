some_list = [1, 2, 3, 4, 5]

for i in some_list:
    some_list.remove(i)
    for n in some_list:
        print(n)
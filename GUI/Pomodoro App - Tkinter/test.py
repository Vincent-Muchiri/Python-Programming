import time
for i in range(5, 0, -1):
    if i <= 0:
        for k in range(20):
            print(k)
            time.sleep(0.3)
    else:
        for j in range(25):
            print(j)
            time.sleep(0.3)
    for l in range(5):
        print(l)
        time.sleep(0.3)

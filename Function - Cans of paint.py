import math

def paint_calc(height, width, cover):
    num_of_cans = height * width / coverage
    # print(num_of_cans)
    #The ceil function rounds up the figure
    print(f"You'll need {math.ceil(num_of_cans)} cans of paint")

test_h = int(input("Input the height of the wall: "))
test_w = int(input("Input the wight of the wall: "))
coverage = 5

paint_calc(height = test_h, width = test_w, cover = coverage)
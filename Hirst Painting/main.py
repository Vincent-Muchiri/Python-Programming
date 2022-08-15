import random
import turtle

import colorgram

rgb_colours = []
colours = colorgram.extract('image.jpg', 120)
for colour in colours:
    # rgb_colours.append(colour.rgb)
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b

    new_colour = (r, g, b)
    rgb_colours.append(new_colour)

print(rgb_colours)
colour_list = [(58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171), (224, 234, 230), (142, 178, 203), (139, 82, 105), (208, 90, 69), (188, 80, 120), (69, 105, 90), (133, 182, 135), (133, 133, 74), (64, 156, 92), (47, 156, 193), (183, 192, 201), (213, 177, 191), (19, 58, 92), (20, 68, 113), (113, 123, 149), (227, 174, 166), (172, 203, 183), (156, 206, 217), (69, 58, 47), (72, 64, 53), (111, 46, 59), (53, 70, 64), (119, 46, 39), (48, 65, 61)]
print(len(colour_list))

i = 0
j = 0
for row in range(10):
    for col in range(10):
        turtle.penup()
        turtle.colormode(255)
        turtle.dot(20, random.choice(colour_list))
        turtle.forward(50)
        i += 1

    j += 50
    turtle.goto(0, j)

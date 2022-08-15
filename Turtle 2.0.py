import turtle
from turtle import Turtle, Screen
import random
timmy = Turtle()

# for num in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# for num in range(15):
#     timmy.pendown()z
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

direction = [0, 90, 180, 270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "Light sea green"]
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_tuple = (r, g, b)
    return random_tuple




# while False:
#     timmy.pendown()
#     timmy.pensize(7)
#     timmy.speed(100)
#     timmy.color(random.choice(colours))
#     # timmy.color(random_colour())
#     timmy.setheading(random.choice(direction))
#     timmy.forward(20)

def draw_spiragraph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.pensize(3)
        timmy.speed("fastest")
        turtle.colormode(255)
        timmy.color(random_colour())
        # timmy.color(random.choice(colours))
        timmy.circle(70)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + 10)

draw_spiragraph(5)


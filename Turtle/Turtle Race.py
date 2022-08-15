import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle olympics")

all_turtle = []


def turtle_create(colours, x_start, y_start, space):
    for elem in colours:
        turtle_name = Turtle(shape="turtle")
        turtle_name.color(elem)
        turtle_name.penup()
        turtle_name.goto(x_start, y_start)
        y_start += space
        all_turtle.append(turtle_name)


colours = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_create(colours, -230, -100, 50)
# print(len(all_turtle))
# print(all_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Select your champion:").lower()

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 215:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print("You've won!")
            else:
                print(f"You've lost. The {winning_colour} turtle is the winner.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

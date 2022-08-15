import turtle
from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def clockwise():
    # tim.forward(10)
    tim.right(10)


def counter_clockwise():
    # tim.back(10)
    tim.left(10)


def clear_screen():
    tim.clear()


def return_origin():
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="space", fun=return_origin)

screen.exitonclick()

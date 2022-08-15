from turtle import Turtle, Screen

tim = Turtle() #Created an object using a class
screen = Screen()


def move_forwards():
    tim.forward(10)

screen.listen() #object.method
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()

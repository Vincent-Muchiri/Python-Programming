import random
from turtle import Turtle
from random import Random
RANDOM_POSITION = random.randint(0,359)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")


    def move_ball(self):
        self.setheading(RANDOM_POSITION)
        # if self.ycor() < -200:
        #     self.setheading(90)
        #     self.forward(0)

    def bounce(self):
        current_heading = self.heading()
        if self.ycor() >= 280:
            self.setheading(current_heading + 270)
        elif self.ycor() <= -280:
            self.setheading(current_heading + 270)

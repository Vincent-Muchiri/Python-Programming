from turtle import Turtle
import random

INITIAL_POSITION = (random.randint(-280, 280), random.randint(-280, 280))


# class Food:
#     def create_food(self):
#         self.food = Turtle()
#         self.food.shape("circle")
#         self.food.shapesize(.8, .8)
#         self.food.color("blue")
#         self.food.penup()
#         self.food.goto(STARTING_POSITION)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.penup()
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 290), random.randint(-280, 290))

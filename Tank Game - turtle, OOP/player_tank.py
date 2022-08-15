import turtle
from turtle import Turtle

# TODO Register the enemy images
turtle.register_shape("./images/Player Tank/Right.gif")
turtle.register_shape("./images/Player Tank/Up.gif")
turtle.register_shape("./images/Player Tank/Left.gif")
turtle.register_shape("./images/Player Tank/Down.gif")

# TODO Create a heading and image pair tuple
RIGHT = (0, "./images/Player Tank/Right.gif")
UP = (90, "./images/Player Tank/Up.gif")
LEFT = (180, "./images/Player Tank/Left.gif")
DOWN = (270, "./images/Player Tank/Down.gif")


class Player(Turtle):
    def __int__(self):
        super().__init__()

    def create(self):
        player_tank = Turtle()
        player_tank.shape(UP[1])
        player_tank.setheading(UP[0])

    def move_left(self):
        self.penup()
        self.shape(LEFT[1])
        self.setheading(LEFT[0])
        self.forward(20)

    def move_right(self):
        self.penup()
        self.shape(RIGHT[1])
        self.setheading(0)
        self.forward(20)
        print(self.xcor())

    def move_up(self):
        self.penup()
        self.shape(UP[1])
        self.setheading(90)
        self.forward(20)
        print(self.ycor())

    def move_down(self):
        self.penup()
        self.shape(DOWN[1])
        self.setheading(270)
        self.forward(20)
        print(self.ycor())


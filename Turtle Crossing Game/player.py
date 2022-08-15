from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        # self.shapesize(2, 2)
        self.goto(0, -270)
        self.setheading(90)
        # self.hideturtle()

    def up(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def left(self):
        self.goto(self.xcor() - 10, self.ycor())
        if self.xcor() <= -380:
            self.goto(-380, self.ycor())

    def right(self):
        self.goto(self.xcor() + 10, self.ycor())
        if self.xcor() >= 380:
            self.goto(380, self.ycor())

    def reset(self):
        self.goto(0, -270)


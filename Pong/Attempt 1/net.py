from turtle import Turtle


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.pensize(5)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 300)
        self.setheading(270)

    def create_net(self):
        for i in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

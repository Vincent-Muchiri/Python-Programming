from turtle import Turtle


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 400)
        self.pensize(5)
        self.pencolor("white")
        self.setheading(270)
        self.hideturtle()

    def create_net(self):
        for i in range(30):
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)


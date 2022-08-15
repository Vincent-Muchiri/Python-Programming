from turtle import Turtle, Screen

screen = Screen()


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")

    def create_paddle(self, position):
        if position == "left":
            self.goto(-350, self.ycor())
        else:
            self.goto(350, self.ycor())

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)
        # TODO Limit the paddle within the screen height
        if self.ycor() >= 240:
            self.goto(self.xcor(), 240)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
        # TODO Limit the paddle within the screen height
        if self.ycor() <= -240:
            self.goto(self.xcor(), -240)

    def reset(self):
        self.goto(self.xcor(), 0)

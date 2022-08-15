from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_point = 0
        self.r_point = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_point, False, "center", font=("Courier", 80, "normal"))
        self.goto(100, 180)
        self.write(self.r_point, False, "center", font=("Courier", 80, "normal"))

    def l_score(self):
        self.l_point += 1
        self.update()

    def r_score(self):
        self.r_point += 1
        self.update()

    def reset(self, left_paddle, right_paddle, ball):
        left_paddle.goto(left_paddle.xcor(), 0)
        right_paddle.goto(right_paddle.xcor(), 0)
        ball.goto(0, 0)
        ball.x_change *= -1
        ball.ball_speed = 0.1



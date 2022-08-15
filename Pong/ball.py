from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_change = 10
        self.y_change = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_change
        new_y = self.ycor() + self.y_change
        self.goto(new_x, new_y)

        # self.setheading(45)
        # self.forward(10)
    def wall_bounce(self):
        self.y_change *= -1

    def paddle_bounce(self):
        self.x_change *= -1
        self.ball_speed /= 1.1


    def reset(self):
        self.goto(0, 0)
        self.x_change *= -1

        # current_heading = self.heading()
        # self.setheading(current_heading + 270)

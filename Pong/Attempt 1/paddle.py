from turtle import Turtle

PADDLE_LENGTH = 6



class Paddle():
    def __init__(self):
        self.paddle_segments = []

    def create_paddle(self, side):
        if side == "left":
            xcor = -380
        else:
            xcor = 350
        J = 20
        for i in range(PADDLE_LENGTH):
            paddle_segment = Turtle()
            paddle_segment.penup()
            paddle_segment.shape("square")
            paddle_segment.color("white")
            paddle_segment.setheading(0)
            paddle_segment.goto(xcor, J)
            J += 20
            paddle_segment.setheading(0)
            self.paddle_segments.append(paddle_segment)

    def move_paddle(self):
        if self.paddle_segments[0].heading() == 90 and self.paddle_segments[0].ycor() < 180:
            for seg in self.paddle_segments:
                seg.setheading(90)
                seg.forward(1)
        elif self.paddle_segments[0].heading() == 270 and self.paddle_segments[0].ycor() > -280:
            for seg in self.paddle_segments:
                seg.setheading(270)
                seg.forward(1)
        else:
            for seg in self.paddle_segments:
                seg.forward(0)

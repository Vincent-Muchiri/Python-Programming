import random
from turtle import Screen, Turtle
from net import Net
import time
from paddle import Paddle
from ball import Ball

# TODO Create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

# TODO Create net
net = Net()
net.create_net()
screen.update()

# TODO Create paddles
left_paddle = Paddle()
right_paddle = Paddle()
left_paddle.create_paddle("left")
right_paddle.create_paddle("right")
screen.update()

# print(len(left_segments))

# TODO Create ball
ball = Ball()
screen.update()

# TODO Move ball
ball.move_ball()

# TODO Set up key bindings
def left_up():
    left_paddle.paddle_segments[0].setheading(90)

def right_up():
    right_paddle.paddle_segments[0].setheading(90)

def left_down():
    left_paddle.paddle_segments[0].setheading(270)

def right_down():
    right_paddle.paddle_segments[0].setheading(270)

screen.listen()
screen.onkey(right_up, "Up")
screen.onkey(right_down, "Down")
screen.onkey(left_up, "w")
screen.onkey(left_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(0.2)
    ball.forward(20)
    screen.update()
    # TODO Move paddle
    left_paddle.move_paddle()
    right_paddle.move_paddle()
    ball.bounce()


    screen.update()


# TODO Move ball and paddle
# TODO Detect collision with wall and bounce
# TODO Detect collision with paddle
# TODO Update score
# TODO Detect when paddle misses


screen.exitonclick()

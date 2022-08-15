import time
from turtle import Screen, Turtle
from net import Net
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# TODO Create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# TODO Create net
net = Net()
net.create_net()

# TODO Create paddles
left_paddle = Paddle()
right_paddle = Paddle()
# left_paddle.forward(20)
left_paddle.create_paddle("left")
right_paddle.create_paddle("right")
screen.update()


# # TODO Create ball
ball = Ball()

# TODO Create scoreboard
scoreboard = Scoreboard()
scoreboard.update()


# # TODO Set up key strokes
screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

ball.move()
is_game_on = True
while is_game_on:
    # print(left_paddle.ycor())
    ball.move()
    time.sleep(ball.ball_speed)
    # print(ball.ycor())
    # TODO Bounce of the wall
    if ball.ycor() >= 277 or ball.ycor() <= -277:
        ball.wall_bounce()
        # current_heading = ball.heading()
        # ball.setheading(current_heading + 270)
        # print("Heading set")
    # TODO Bounce of the paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() >= 330 or ball.distance(left_paddle) < 50 and \
            ball.xcor() <= -330:
        ball.paddle_bounce()

    # TODO Detect whether paddle missed the ball
    if ball.xcor() >= 390:
        scoreboard.l_score()
        scoreboard.reset(left_paddle, right_paddle, ball)
        # ball.reset()
        # left_paddle.reset()
        # right_paddle.reset()
        screen.update()
        time.sleep(5)
    elif ball.xcor() <= -390:
        scoreboard.r_score()
        scoreboard.reset(left_paddle, right_paddle, ball)
        # ball.reset()
        # left_paddle.reset()
        # right_paddle.reset()
        screen.update()
        time.sleep(5)



    screen.update()

screen.exitonclick()

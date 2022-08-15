import random
import time
import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# TODO Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)  # Turn animation on and set a delay for updating drawing

# TODO Create starting snake
snake = Snake()
# snake.create_snake() #This makes the snake twice as long
screen.update()

# TODO Create food
food = Food()
screen.update()

# TODO Create scoreboard
scoreboard = Scoreboard()
screen.update()

# TODO Set up key strokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # TODO Move snake
    snake.move()

    # TODO Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        # scoreboard.update_score()
        scoreboard.increase_score()
            # print(score)

    # TODO Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # print(f"Game over! You've scored {scoreboard.score} points")
        scoreboard.reset()
        snake.reset()
        snake.move()
        # scoreboard.game_over()
        # game_is_on = False

    # TODO Detect collision with tail
    for seg in snake.segments[1:]:
        # if seg == snake.head:
        #     pass
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()
            # scoreboard.game_over()
            # game_is_on = False




screen.exitonclick()

import random
import time
from turtle import Screen, Turtle
from player import Player
from scoreboard import Scoreboard
from car_manager import Car_manager

# TODO Create screen
screen = Screen()
screen.setup(800, 600)
screen.title("Crossing Game")
screen.bgcolor("grey")
screen.tracer(0)

# TODO Create turtle
player = Player()
screen.update()

# Todo Create cars
car_manager = Car_manager()
screen.update()

# TODO Create scoreboard
scoreboard = Scoreboard()
scoreboard.create()
screen.update()


# TODO Set key bindings
screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create()
    car_manager.move()

    # # TODO Update scoreboard
    # if player.ycor() >= 280:
    #     scoreboard.next_level(player)
    #     car_manager.level_up()
    #
    # # TODO Detect collision
    # for car in car_manager.all_cars:
    #     if car.distance(player) <= 29:
    #         scoreboard.game_over()
    #         is_game_on = False

screen.exitonclick()

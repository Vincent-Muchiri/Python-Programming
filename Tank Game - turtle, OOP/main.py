# -------------------------------------------------------- IMPORTS -----------------------------------------------------
import turtle
from turtle import Screen, Turtle
from enemy_manager import EnemyTank
from player_tank import Player
import time

# ---------------------------------------------- CONSTANTS & GLOBAL VARIABLES ------------------------------------------


# ------------------------------------------------------- FUNCTIONS ----------------------------------------------------



# def enemy_tanks():
#     # TODO Create enemy tanks
#     enemy_turtle = Turtle()
#     enemy_turtle.penup()
#     enemy_turtle.shape("images/Enemy Tank.gif")
#
#     # TODO Place the enemy turtles randomly on the scree
#     enemy_turtle.goto(100, 100)


# def shoot():
#     player_xcor = player_turtle.xcor()
#     player_ycor = player_turtle.ycor()
#
#     # TODO Create bullet
#     bullet = Turtle()
#     bullet.hideturtle()
#     bullet.shape("square")
#     bullet.shapesize(0.5)
#     bullet.penup()
#
#     bullet.goto(player_xcor, player_ycor)
#     bullet.setheading(player_turtle.heading())
#     bullet.forward(20)
#     screen.update()
#     bullet.showturtle()


# ------------------------------------------------------ GUI -----------------------------------------------------------
# TODO Setup the screen
screen = Screen()
screen.setup(width=700, height=500)
screen.title("Tank Game")
screen.bgcolor("white")
screen.tracer(0)


# TODO Create boundary
boundary = Turtle()
boundary.penup()
boundary.hideturtle()
boundary.pensize(5)
boundary.goto(230, 250)
boundary.pendown()
boundary.goto(230, -250)
screen.update()


# TODO Create the tank
player_turtle = Player()
player_turtle.create()
screen.update()

# TODO Create movement
screen.listen()
screen.onkey(player_turtle.move_left, "Left")
screen.onkey(player_turtle.move_up, "Up")
screen.onkey(player_turtle.move_down, "Down")
screen.onkey(player_turtle.move_right, "Right")

# TODO Create enemy tank
enemy_tanks = EnemyTank()
enemy_tanks.create()
screen.update()

is_game_on = True
while is_game_on:
    screen.update()
    player_xcor = player_turtle.xcor()
    player_ycor = player_turtle.ycor()

    # TODO Maintain boundary
    if player_xcor >= 103:
        player_turtle.goto(103, player_ycor)
    if player_xcor <= -224:
        player_turtle.goto(-224, player_ycor)
    if player_ycor >= 224:
        player_turtle.goto(player_xcor, 224)
    if player_ycor <= -218:
        player_turtle.goto(player_xcor, -218)


screen.exitonclick()

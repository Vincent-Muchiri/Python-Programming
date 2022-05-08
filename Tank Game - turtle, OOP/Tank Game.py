from turtle import Turtle, Screen
import turtle
import random
import time

STARTING_POSITION = (-150, 0)


def border():
    player_xcor = player_tank.xcor()
    player_ycor = player_tank.ycor()

    # TODO Right border
    if player_xcor <= -370:
        player_tank.goto(-370, player_ycor)
    if player_xcor >= 70:
        player_tank.goto(70, player_ycor)
    if player_ycor <= -220:
        player_tank.goto(player_xcor, -220)
    if player_ycor >= 220:
        player_tank.goto(player_xcor, 220)


def prevent_overlap():
    for tank in enemy_tanks_list:
        if tank.distance(player_tank) <= 50:
            player_tank.goto(player_tank.xcor(), player_tank.ycor())


def move_right():
    player_tank.setheading(0)
    player_tank.shape("./images/Player Tank/Right.gif")
    player_tank.forward(20)


def move_up():
    player_tank.setheading(90)
    player_tank.shape("./images/Player Tank/Up.gif")
    player_tank.forward(20)


def move_left():
    player_tank.setheading(180)
    player_tank.shape("./images/Player Tank/Left.gif")
    player_tank.forward(20)


def move_down():
    player_tank.setheading(270)
    player_tank.shape("./images/Player Tank/Down.gif")
    player_tank.forward(20)


def move_enemy_tanks():
    for enemy in enemy_tanks_list:
        print(enemy)
        enemy_tanks_list.remove(enemy)
        for tank in enemy_tanks_list:
            print(enemy_tanks_list)
            # print(enemy.distance(tank))
            # if enemy.distance(tank) <= 10:
            #     heading_image_pair = random.choice(HEADING_IMAGE_TUPLE)
            #     tank.setheading(heading_image_pair[0])
            #     tank.shape(heading_image_pair[1])
            # else:
            #     enemy.forward(20)



# TODO Create screen
window = Screen()
window.title("Tank Game")
window.setup(800, 500, 100, 100)
window.tracer(0)

# TODO Register player images
turtle.register_shape("./images/Player Tank/Left.gif")
turtle.register_shape("./images/Player Tank/Up.gif")
turtle.register_shape("./images/Player Tank/Down.gif")
turtle.register_shape("./images/Player Tank/Right.gif")

# TODO Register enemy images
turtle.register_shape("./images/Enemy Tank/Down.gif")
turtle.register_shape("./images/Enemy Tank/Left.gif")
turtle.register_shape("./images/Enemy Tank/Up.gif")
turtle.register_shape("./images/Enemy Tank/Right.gif")

# TODO Create an image pair
HEADING_IMAGE_TUPLE = (
                          (90, "./images/Enemy Tank/Up.gif"),
                          (270, "./images/Enemy Tank/Down.gif"),
                          (180, "./images/Enemy Tank/Left.gif"),
                          (0, "./images/Enemy Tank/Right.gif")
)

# TODO Create border
borderline = Turtle()
borderline.hideturtle()
borderline.penup()
borderline.goto(100, 250)
borderline.pendown()
borderline.pensize(5)
borderline.goto(100, -250)
window.update()

# TODO Create player tank
player_tank = Turtle()
player_tank.penup()
player_tank.goto(STARTING_POSITION)
player_tank.shape("./images/Player Tank/Up.gif")
window.update()

enemy_tanks_list = []
# TODO Create enemy tanks
for tanks in range(4):
    enemy_tank = Turtle()
    enemy_tank.penup()
    heading_image_pair = random.choice(HEADING_IMAGE_TUPLE)
    enemy_tank.setheading(heading_image_pair[0])
    enemy_tank.shape(heading_image_pair[1])

    # TODO Place enemy tanks randomly
    random_xcor = random.randint(-370, 70)
    random_ycor = random.randint(-220, 220)
    enemy_tank.goto(random_xcor, random_ycor)

    enemy_tanks_list.append(enemy_tank)


# TODO Create movement
window.listen()
window.onkey(move_up, "Up")
window.onkey(move_down, "Down")
window.onkey(move_right, "Right")
window.onkey(move_left, "Left")

is_game_on = True

while is_game_on:
    window.update()
    border()
    move_enemy_tanks()
    time.sleep(0.5)


    # prevent_overlap()

window.exitonclick()

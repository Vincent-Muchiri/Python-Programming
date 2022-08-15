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


# def move_enemy_tanks():
#     new_tank_list = []
#     new_tank_list = enemy_tanks_list
#     for enemy in new_tank_list:
#         new_tank_list.remove(enemy)
#         for tank in new_tank_list:
#             # print(enemy_tanks_list)
#             # print(enemy.distance(tank))
#             if enemy.distance(tank) <= 10:
#                 heading_image_pair = random.choice(HEADING_IMAGE_TUPLE)
#                 tank.setheading(heading_image_pair[0])
#                 tank.shape(heading_image_pair[1])
#                 print("Collision imminent")
#             else:
#                 print("Forward")
#                 enemy.forward(20)




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

print(player_tank)
all_tanks_list = [player_tank]

# TODO Create enemy tanks
for tanks in range(10):
    enemy_tank = Turtle()
    enemy_tank.penup()
    heading_image_pair = random.choice(HEADING_IMAGE_TUPLE)
    enemy_tank.setheading(heading_image_pair[0])
    enemy_tank.shape(heading_image_pair[1])

    enemy_tanks_list.append(enemy_tank)
    all_tanks_list.append(enemy_tank)

    # TODO Place enemy tanks randomly
    random_xcor = random.randint(-370, 70)
    random_ycor = random.randint(-220, 220)
    enemy_tank.goto(random_xcor, random_ycor)

    overlapping = True
    count=0

    while overlapping:
        count+=1
        distances = []
        for tank in all_tanks_list[:-1]:
            distances.append(tank.distance(enemy_tank))

        print(distances)

        for dis in distances:
            if dis <= 60:
                random_xcor = random.randint(-370, 70)
                random_ycor = random.randint(-220, 220)
                enemy_tank.goto(random_xcor, random_ycor)
            else:
                overlapping = False

    print(count)
    # # TODO Place enemy tanks randomly
    # random_xcor = random.randint(-370, 70)
    # random_ycor = random.randint(-220, 220)
    # enemy_tank.goto(random_xcor, random_ycor)
    #
    # # TODO Check whether the tanks overlap
    # current_tank = all_tanks_list[-1]
    # print(len(all_tanks_list))

    # for tank in all_tanks_list[:-1]:
    #     print(f"{tank} - {current_tank} = {tank.distance(current_tank)}")
    #     if tank.distance(current_tank) <= 60:
    #         print("Overlap")
    #         random_xcor = random.randint(-370, 70)
    #         random_ycor = random.randint(-220, 220)
    #         current_tank.goto(random_xcor, random_ycor)
    #         print(tank.distance(current_tank))
    #
    #     else:
    #         tank_overlap = False
    #         print("No overlap")
    #
    # still_overlapping = True
    # while still_overlapping:
    #     for tank in all_tanks_list[:-1]:
    #         print(f"{tank} - {current_tank} = {tank.distance(current_tank)}")
    #         if tank.distance(current_tank) <= 60:
    #             print("Overlap")
    #             random_xcor = random.randint(-370, 70)
    #             random_ycor = random.randint(-220, 220)
    #             current_tank.goto(random_xcor, random_ycor)
    #             print(tank.distance(current_tank))
    #         else:
    #             still_overlapping = False
    #             print("No overlap")

    print("")

# TODO Check whether there is still an overlap
for tank in all_tanks_list:
    for t in all_tanks_list:
        dis = tank.distance(t)
        if dis == 0:
            pass
        elif dis <= 60:
            print(dis)


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
    # move_enemy_tanks()
    time.sleep(0.1)


    # prevent_overlap()

window.exitonclick()

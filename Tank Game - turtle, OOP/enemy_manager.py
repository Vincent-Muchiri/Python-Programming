from turtle import Turtle
import turtle
import random


# TODO Register the enemy images
turtle.register_shape("./images/Enemy Tank/Right.gif")
turtle.register_shape("./images/Enemy Tank/Up.gif")
turtle.register_shape("./images/Enemy Tank/Left.gif")
turtle.register_shape("./images/Enemy Tank/Down.gif")

# TODO Create a heading and image pair tuple
HEADING_IMAGE_PAIR = (
    (0, "./images/Enemy Tank/Right.gif"),
    (90, "./images/Enemy Tank/Up.gif"),
    (180, "./images/Enemy Tank/Left.gif"),
    (270, "./images/Enemy Tank/Down.gif")
)


class EnemyTank(Turtle):
    def __int__(self):
        super().__init__()
        # TODO Create the enemy tank attributes
        self.hideturtle()
        self.all_tanks = []

    def create(self):
        for index in range(4):
            enemy_tank = Turtle()
            # enemy_tank.hideturtle()
            # TODO Assign a random direction
            enemy_tank.penup()
            start_heading = random.choice(HEADING_IMAGE_PAIR)
            enemy_tank.setheading(start_heading[0])
            enemy_tank.shape(start_heading[1])
            random_x = random.randint(-224, 103)
            random_y = random.randint(-218, 224)
            print(random_x, random_y)

            # TODO Make sure the enemy tank is not placed near the center
            if 60 >= random_x >= 0:
                random_x += 60
            elif 0 >= random_x >= -60:
                random_x -= 60
            if 60 >= random_y >= 0:
                random_y += 60
            elif 0 >= random_y >= -60:
                random_y -= 60

            # print(random_x, random_y)
            # print("")
            enemy_tank.goto(random_x, random_y)
            # print(type(enemy_tank))
            self.all_tanks.append(enemy_tank)



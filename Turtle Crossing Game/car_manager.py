from turtle import Turtle
import random

COLOURS = ("black", "green", "yellow", "red", "purple", "blue", "orange")
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car_manager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create(self):
        random_chance = random.randint(1, 7)
        if random_chance == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.setheading(180)
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLOURS))
            random_y = random.randint(-220, 300)
            random_x = random.randint(400, 420)
            car.goto(random_x, random_y)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed + MOVE_INCREMENT)

    def level_up(self):
        self.car_speed += 1

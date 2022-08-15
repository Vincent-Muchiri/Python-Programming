from turtle import Turtle
from snake import Snake
from food import Food


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.goto(0, 278)
        self.color("white")
        self.write(f"Score: {self.score} High score: {self.high_score}" , False, "center", ("Courier", 12, "normal"))
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        # self.score += 1
        self.write(f"Score: {self.score} High score: {self.high_score}", False, "center", ("Courier", 12, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.home()
    #     self.color("red")
    #     self.write(f"GAME OVER!", False, "center", ("Courier", 20, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_score()
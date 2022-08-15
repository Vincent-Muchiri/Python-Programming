from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.color("white")
        self.penup()

    def create(self):
        self.clear()
        self.goto(-360, 280)
        self.write(f"Level {self.level}", False, "center", font=("Courier", 12, "normal"))

    def next_level(self, player):
        self.level += 1
        self.create()
        player.reset()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, "center", font=("Courier", 20, "bold"))


from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.goto(-270, 250)
        self.write(f"Level: {self.level} ", align="left", font=("Arial", 20, "normal"))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level} ", align="left", font=("Arial", 20, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER ", align="center", font=("Arial", 20, "normal"))
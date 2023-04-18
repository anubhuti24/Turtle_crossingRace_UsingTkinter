from turtle import Turtle

STARTING_POS = (0, -270)
MOVE = 10
FINISH_LINE = 276


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=1.5)
        self.goto(STARTING_POS)
        self.setheading(90)

    def up(self):
        self.forward(MOVE)

    def go_to_start(self):
        self.goto(STARTING_POS)

    def is_finish(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False



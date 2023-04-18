from turtle import Turtle
import random
color = ["red", "orange", "blue", "green", "pink", "brown", "purple"]
STARTING_DIS = 6
MOVE_INCREMENT = 5


class Cars():
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_DIS

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new = Turtle()
            new.shape("square")
            new.shapesize(stretch_wid=1, stretch_len=2)
            new.penup()
            new.color(random.choice(color))
            random_y = random.randint(-235, 240)
            new.goto(300, random_y)
            self.all_cars.append(new)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT


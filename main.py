from turtle import Turtle, Screen
import time
from player import Player
from car_manager import Cars
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
player1 = Player()
Car = Cars()
scores = Score()


screen.listen()
screen.onkey(player1.up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    Car.create_car()
    Car.move_car()

    # DETECT COLLISION OF TURTLE WITH CARS
    for car in Car.all_cars:
        if car.distance(player1) < 33:
            game_is_on = False
            scores.game_over()

    if player1.is_finish():
        Car.increase_speed()
        scores.increase_level()
        player1.go_to_start()


screen.exitonclick()
import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

t = Player()
screen.onkey(t.go_up, "Up")

scoreboard = Scoreboard()

car_manager = CarManager()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()
    # Detect collision with the car
    for car in car_manager.all_cars:
        if t.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    if t.is_finished():
        scoreboard.update()
        t.reset_position()
        car_manager.level_up()


screen.exitonclick()

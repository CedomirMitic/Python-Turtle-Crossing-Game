import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(fun=player.up, key="Up")
number = float(random.randint(-265, 280))
car = CarManager((300, number))
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move()

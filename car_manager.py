from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.color(random.choice(COLORS))
        self.tilt(90)
        self.goto(position)

    def move(self):
        position = self.xcor()
        moving = position - MOVE_INCREMENT
        self.goto(moving , self.ycor())
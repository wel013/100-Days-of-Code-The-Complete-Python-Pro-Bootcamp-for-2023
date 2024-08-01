from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        # should be a 10 by 10 turtle
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.shift_new_loc()

    def shift_new_loc(self):
        randx = random.randint(-270, 270)
        randy = random.randint(-270, 270)
        self.goto(randx, randy)

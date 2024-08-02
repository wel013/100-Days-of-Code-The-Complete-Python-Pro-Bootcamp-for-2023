from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, side) -> None:
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=5)
        self.setheading(90)
        if side == "r":
            self.goto(350, 0)
        elif side == "l":
            self.goto(-350, 0)

    def up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        self.goto(self.xcor(), self.ycor()-30)

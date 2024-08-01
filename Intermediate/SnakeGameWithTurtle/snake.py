from turtle import Screen, Turtle


class Snake():

    def __init__(self, move_step) -> None:
        self.move_step = move_step
        self.segments = []
        self.create_snake()
        self.UP = 90
        self.LEFT = 180
        self.RIGHT = 0
        self.DOWN = 270

    def create_snake(self):
        t0 = Turtle(shape="square")

        t1 = Turtle(shape="square")
        t2 = Turtle(shape="square")
        t0.color("white")
        t0.penup()

        t1.color("white")
        t1.penup()

        t1.setposition(t0.xcor()-20, t0.ycor())

        t2.color("white")
        t2.penup()

        t2.setposition(t1.xcor()-20, t0.ycor())
        self.segments = [t0, t1, t2]

    def snake_move(self):
        for i in range(len(self.segments)-1, 0, -1):
            newx = self.segments[i-1].xcor()
            newy = self.segments[i-1].ycor()
            self.segments[i].goto(newx, newy)
        self.segments[0].forward(self.move_step)

    def up(self):
        if self.segments[0].heading() != self.DOWN:
            self.segments[0].setheading(90)

    def left(self):
        if self.segments[0].heading() != self.RIGHT:

            self.segments[0].setheading(180)

    def down(self):
        if self.segments[0].heading() != self.UP:

            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != self.LEFT:

            self.segments[0].setheading(0)

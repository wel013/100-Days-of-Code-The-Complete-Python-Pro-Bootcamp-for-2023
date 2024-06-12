from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.left(90)
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.fd(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def is_finished(self):
        if self.ycor() > 280:
            return True
        return False









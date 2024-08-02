from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("slow")
        self.x_move = 10
        self.y_move = 10
        self.speed_cur = 0.1

    def update_loc(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bounce(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_paddle()
        self.speed_cur = 0.1

    def speed_up(self):
        self.speed_cur *= 0.9

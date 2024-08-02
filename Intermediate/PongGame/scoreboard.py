from turtle import Turtle

ALIGNMENT = "center"
FONTS = ('Arial', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.left_score = 0
        self.right_score = 0

        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.goto(x=-100, y=180)
        self.write(
            self.left_score, False, align=ALIGNMENT, font=FONTS)
        self.goto(x=100, y=180)
        self.write(
            self.right_score, False, align=ALIGNMENT, font=FONTS)

    def gain_points_left(self):
        self.left_score += 1
        self.clear()
        self.update_score_board()

    def gain_points_right(self):
        self.right_score += 1
        self.clear()
        self.update_score_board()

    def gameover(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER!", False, align=ALIGNMENT, font=FONTS)

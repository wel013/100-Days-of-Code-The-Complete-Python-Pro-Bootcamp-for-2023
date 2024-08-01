from turtle import Turtle

ALIGNMENT = "center"
FONTS = ('Arial', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.current_score = 0
        self.goto(x=0, y=270)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.write(
            f"Current Score: {self.current_score}", False, align=ALIGNMENT, font=FONTS)

    def gain_points(self):
        self.current_score += 1
        self.clear()
        self.update_score_board()

    def gameover(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER!", False, align=ALIGNMENT, font=FONTS)

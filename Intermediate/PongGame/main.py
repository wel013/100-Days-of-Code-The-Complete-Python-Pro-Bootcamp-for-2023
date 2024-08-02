from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Name")
screen.tracer(0)

p1 = Paddle("r")
p2 = Paddle("l")

ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(p1.up, "Up")
screen.onkeypress(p1.down, "Down")
screen.onkeypress(p2.up, "w")
screen.onkeypress(p2.down, "s")
# when the tracer is off, need to constantly update the screen
game_is_on = True

while game_is_on:
    # pause the loop st that ball move at a reasonable speed
    time.sleep(ball.speed_cur)
    screen.update()
    ball.update_loc()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # detection with paddle
    if (ball.distance(p1) < 50 and ball.xcor() > 320) or (ball.distance(p2) < 50 and ball.xcor() < -320):
        ball.bounce_paddle()
        ball.speed_up()
    if (ball.distance(p1) > 50 and ball.xcor() > 380):
        ball.reset_position()
        scoreboard.gain_points_left()
    if (ball.distance(p2) > 50 and ball.xcor() < -380):
        ball.reset_position()
        scoreboard.gain_points_right()


screen.exitonclick()

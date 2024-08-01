from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Name")
screen.tracer(0)
screen.listen()


snake = Snake(20)
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

screen.onkey(snake.left, "Left")

screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    # move snake
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
screen.exitonclick()

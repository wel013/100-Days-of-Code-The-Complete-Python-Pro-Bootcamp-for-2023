from turtle import Turtle, Screen
from random import randint
colors = ["red", "orange", "pink", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False

turtle_list = []
# E = 0, N = 90, W=180, S = 270
for i in range(6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x=-240, y=-150+i*60)
    turtle_list.append(turtle)

user_choice = screen.textinput(
    title="Pick Your Fighter", prompt="Type a color from the turtles: ")

if user_choice:
    is_race_on = True

winner = ""
while is_race_on:
    for t in turtle_list:
        if t.xcor() >= 220:
            is_race_on = False
            winner = t.color()[0]
        step = randint(0, 10)
        t.forward(step)

if winner == user_choice:
    print(f"You won, the {winner} turtle was the fastest")
else:
    print(f"oops you lost, the winner is the {winner} turtle")

screen.exitonclick()

from turtle import Turtle, Screen, colormode
from random import randint
import colorgram

colormode(255)

t = Turtle()
t.hideturtle()
colors = colorgram.extract('image.jpg', 10)
color_rgb = []
for color in colors:
    rgb = (color.rgb[0], color.rgb[1], color.rgb[2])
    color_rgb.append(rgb)
tp = t.pos()
tp = (tp[0]-100, tp[1]-100)

t.penup()
for i in range(10):
    new_x = tp[0] + 50*i
    t.setpos((tp[1], new_x))
    for _ in range(10):  # draws a row
        ranNum = randint(0, len(color_rgb)-1)
        t.pendown()
        t.color(color_rgb[ranNum])
        t.dot(20)
        t.penup()
        t.forward(50)
screen = Screen()
screen.exitonclick()

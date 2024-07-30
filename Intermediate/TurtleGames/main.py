from turtle import Turtle, Screen
t = Turtle()


def move_forwards():
    t.forward(10)


def move_backward():
    t.backward(10)


def move_counterclock():
    # t.left(10)
    new_heading = t.heading() + 10
    t.setheading(new_heading)


def move_clock():
    t.right(10)
    new_heading = t.heading() - 10
    t.setheading(new_heading)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()



t.speed(10)
screen = Screen()
screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=move_counterclock)
screen.onkeypress(key="d", fun=move_clock)
screen.onkeypress(key="c", fun=clear)
screen.exitonclick()

import random
from flask import Flask

app = Flask(__name__)

radnum = random.randint(0, 9)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route("/")
@make_bold
# @make_underline
def hello_world():
    return "<p>Enter a number from 0 to 9 in the URL!</p>"


@app.route("/<int:number>")
def greet_user(number):
    if number == radnum:
        return f"<h1>Just Right! </h1> <img src = https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXZidzR5djZ1aTRrcXI3d2l1bWwwYjd6OW16eG91ZDdlZWZuZmY0YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Diym3aZO1dHzO/giphy.webp>"
    if number < radnum:
        return f"<p>Too Low!</p> <br> <img src = https://static1.cbrimages.com/wordpress/wp-content/uploads/2019/11/Eva-Funny-Feature.jpg>"
    if number > radnum:
        return f"<p> Too High!</p> <br> <img src = https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2ZremIxMGFyN2dycTBzazl6djdyZnE1dDRkMDJ4enRhZ3VpeGdmYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l5IcRY8ZIR6yQ/200w.webp>"


if __name__ == "__main__":
    app.run(debug=True)

from pandas import *
from random import *
from tkinter import *
from tkinter import messagebox




#---------------------------------------READING WORDS FROM THE CSV AND REPLACE THE LABEL WITH ACTUAL WORDS---------------------------------------#
word_dict = {}

try:
    data = read_csv("data/need_to_learn.csv")
except FileNotFoundError:
    ori_data = read_csv("data/words_japanese.csv")
    word_dict = ori_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")

card = choice(word_dict)
print(word_dict)
def change_words():
    global card, flip_timer
    #every time get a new card, invalidate the timer and
    window.after_cancel(flip_timer)
    card = choice(word_dict)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(word, text=card["Japanese"], fill="black")
    canvas.itemconfig(card_title, text="Japanese", fill="black")
    #activate the new timer
    flip_timer = window.after(3000, count_down)

def change_words_corret():
    try:
        word_dict.remove(card)
        change_words()
    except IndexError:
        messagebox.showinfo(title="Empty Deck", message="Seems like you have studied all the words, re-start the program to study again")
    else:
        df = DataFrame(word_dict)
        df.to_csv("data/need_to_learn.csv", index=False)
def count_down():
    global card
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(word, text=card["English"], fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")

#---------------------------------------UI---------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, count_down)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file="images\card_back.png")
card_front = PhotoImage(file="images\card_front.png")
right_image = PhotoImage(file="images\correct.png")
wrong_image = PhotoImage(file="images\wrong.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="title", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="trouve", fill="black", font=("Ariel", 60, "bold"))

correct_b = Button(image=right_image, highlightthickness=0, command=change_words_corret)
wrong_b = Button(image=wrong_image, highlightthickness=0, command=change_words)
correct_b.grid(column=0, row=1)
wrong_b.grid(column=1, row=1)
change_words()


window.mainloop()



#try to add a function where it is finished, it shows something
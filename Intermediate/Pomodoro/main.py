from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
COOLER_GREEN = "#C5D8A4"
COOLER_RED = "#B33030"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(the_timer, text="00:00")
    label_timer.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps, timer_end
    reps +=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 2 != 0:
        count = work_sec
        label_timer.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count = long_break_sec
        label_timer.config(text="Long Break", fg=RED)
    else:
        count = short_break_sec
        label_timer.config(text="Short Break", fg=PINK)
    count_down(count)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer, timer_end
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(the_timer, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    elif count == 0:
        start_timer()
        mark = ""
        for i in range(math.floor(reps/2)):
            mark += "🍅"
        check.config(text=mark)
        # Pop up the window to the front when time is up
        timer_end = True
        window.attributes("-topmost", timer_end)
        window.attributes("-topmost", False)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
the_timer = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label_timer.grid(column=1, row=0)

start_b = Button(text="Start", bg=COOLER_GREEN, command=start_timer)
end_b = Button(text="Reset", bg=COOLER_GREEN, command=reset_timer)
start_b.grid(column=0, row=2)
end_b.grid(column=2, row=2)

check = Label(bg=YELLOW, font=(FONT_NAME, 16, "bold"), fg=COOLER_RED)
check.grid(column=1, row=3)



window.mainloop()

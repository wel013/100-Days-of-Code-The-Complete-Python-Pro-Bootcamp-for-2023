THEME_COLOR = "#375362"
#class based GUI
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:
    #add the datatype of QB
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        ######CREATING THE UI######

        self.label = Label()
        self.label.config(text="Score: ", bg=THEME_COLOR, fg="white")
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.word = self.canvas.create_text(150, 125, text="", fill=THEME_COLOR, font=("Ariel", 15, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        correct_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.b_correct = Button(image=correct_image, highlightthickness=0, command=self.click_true)
        self.b_wrong = Button(image=false_image, highlightthickness=0, command=self.click_false)
        self.b_wrong.grid(column=1, row=2)
        self.b_correct.grid(column=0, row=2)

        self.get_next_q()

        self.window.mainloop()

    def get_next_q(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.word, text=q_text)
        else:
            self.canvas.itemconfig(self.word, text="You have finished your quiz!")
            self.b_correct.config(state="disabled")
            self.b_wrong.config(state="disabled")

    def click_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def click_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right:bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_q)


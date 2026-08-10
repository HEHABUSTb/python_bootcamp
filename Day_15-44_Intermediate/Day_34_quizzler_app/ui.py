from tkinter import *
from quiz_brain import QuizBrain
import html

THEME_COLOR = "#375362"
FONT = ('Arial', 15, 'italic')


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # Quiz brains
        self.quiz_brain = quiz_brain

        # Create window
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score counter
        self.score_text = Label(text='Score: 0', bg=THEME_COLOR, fg='white', font=('Courier', 15, 'normal'))
        self.score_text.grid(row=0, column=1)

        # Create Canvas with quiz
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.canvas_text = self.canvas.create_text(150, 75, width=280, text='Some text', fill=THEME_COLOR, font=FONT)

        # Buttons True or False
        image_true = PhotoImage(file='images/true.png')
        self.button_true = Button(image=image_true, highlightthickness=0, command=lambda: self.check_answer('True'))
        self.button_true.grid(row=2, column=0, padx=20, pady=20)

        image_false = PhotoImage(file='images/false.png')
        self.button_false = Button(image=image_false, highlightthickness=0, command=lambda: self.check_answer('False'))
        self.button_false.grid(row=2, column=1)

        # loop
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()

            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached end of the quiz")


    def check_answer(self, answer: str):
        is_right = self.quiz_brain.check_answer(answer)
        self.give_feedback(is_right=is_right)
        self.score_text.config(text=f'Score: {self.quiz_brain.score}')


    def give_feedback(self, is_right: bool):
        if is_right is True:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(ms=900, func=self.next_question)




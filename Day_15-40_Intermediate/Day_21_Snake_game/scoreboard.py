from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0

        self.penup()
        self.hideturtle()
        self.color('white')
        self.sety(y=270)
        self.speed('fastest')

        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Your Score: {self.score}", align='center', font=("Arial", 16, "normal"))


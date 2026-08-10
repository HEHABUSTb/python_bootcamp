from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = 'left'


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 1

        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(x=-270, y=260)
        self.speed('fastest')

        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level:{self.score}", align=ALIGNMENT, font=FONT)

    def game_over_message(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align='center', font=FONT)
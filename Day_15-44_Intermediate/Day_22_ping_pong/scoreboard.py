from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 16, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.score_left = 0
        self.score_right = 0

        self.penup()
        self.hideturtle()
        self.color('white')
        self.sety(y=265)
        self.speed('fastest')

        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score_left}:{self.score_right}", align=ALIGNMENT, font=FONT)

    def game_over_message(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
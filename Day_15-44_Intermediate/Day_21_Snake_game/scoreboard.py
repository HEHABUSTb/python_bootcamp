from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 16, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.high_score = self.read_high_score()

        self.penup()
        self.hideturtle()
        self.color('white')
        self.sety(y=260)
        self.speed('fastest')

        self.update_score()

    def read_high_score(self):
        with open("high_score.txt") as file:
            high_score = file.read()

            return int(high_score)

    def write_high_score(self, high_score: int):
        with open("high_score.txt", mode='w') as file:
            file.write(f"{high_score}")

    def update_score(self):
        self.clear()
        self.write(f"Your Score:{self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score(high_score=self.high_score)
        self.score = 0
        self.update_score()

    # def game_over_message(self):
    #     self.goto(x=0, y=0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

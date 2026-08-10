import random
import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make a bet!', prompt='Which turtle would be win?')
colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple']
turtles = []
y = -90

for color in colors:

    turtle = Turtle(shape='turtle')
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=y)
    y += 30

    turtles.append(turtle)


def check_winner(user_input, turtle_color):
    # Compare winner color of turtle and user input
    if user_input.lower() == turtle_color.lower():
        print(f"Yow was right ! Your {turtle_color} turtle is winner!")
    else:
        print(f"Sorry you lose. {turtle_color} turtle win the game! ")


game_on = True
winner = str

while game_on:

    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        position = turtle.xcor()
        if position >= 230:
            game_on = False
            winner = turtle.pencolor()
            check_winner(user_input=user_bet, turtle_color=winner)
            time.sleep(2)





screen.exitonclick()

import time
from turtle import Screen, Turtle
from Snake import Snake
from Food import Food

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('My Snake game!')


score = Turtle()

counter = 0
score.color('white')
score.penup()
score.sety(y=270)
score.hideturtle()
score.speed('fastest')
score.write(f"Your Score: {counter}", align='center', font=("Arial", 12, "normal"))

time.sleep(2)
counter = 5
score.clear()
score.write(f"Your Score: {counter}", align='center', font=("Arial", 12, "normal"))













screen.exitonclick()
import random, time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('My Ping Pong Game!')
screen.tracer(0)

paddles = Paddle()
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkeypress(fun=paddles.move_left_paddle_up, key='w')
screen.onkeypress(fun=paddles.move_left_paddle_down, key='s')
screen.onkeypress(fun=paddles.move_right_paddle_up, key='Up')
screen.onkeypress(fun=paddles.move_right_paddle_down, key='Down')


game_is_running = True
while game_is_running:
    time.sleep(0.01)
    screen.update()

    ball.move()

    # Collision with y wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_from_wall()

    # Bounce ball from a paddles
    paddle_down = paddles.paddles[0]
    paddle_up = paddles.paddles[1]
    if ball.distance(paddle_down) < 20 or ball.distance(paddle_up) < 20:
        ball.bounce_from_paddle()

    # Counting Score
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.score_right += 1
        scoreboard.update_score()
    elif ball.xcor() > 390:
        ball.reset_position()
        scoreboard.score_left += 1
        scoreboard.update_score()


















screen.exitonclick()
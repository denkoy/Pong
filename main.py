from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800,height=600)
rightPaddle=Paddle()
rightPaddle.setposition(350,0)
leftPaddle=Paddle()
leftPaddle.setposition(-350,0)
ball=Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(rightPaddle.go_up,"Up")
screen.onkey(rightPaddle.go_down,"Down")
screen.onkey(leftPaddle.go_up,"w")
screen.onkey(leftPaddle.go_down,"s")
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    if ball.wall_colissions():
        ball.wall_bounce()
    if ball.paddle_collision(rightPaddle) and ball.xcor()>340:
        ball.paddle_bounce()
        scoreboard.plus("r")
    if ball.paddle_collision(leftPaddle) and ball.xcor()<-340:
        ball.paddle_bounce()
        scoreboard.plus("l")
    if ball.xcor() > 400 or ball.xcor() < -400:
        scoreboard.end_of_game()
        game_is_on=False
    ball.move(ball.compass)



screen.exitonclick()
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

start_speed = 0.1

left_paddle = Paddle(x=-350)
right_paddle = Paddle(x=350)

ball = Ball()

left_score = Scoreboard(x=-70, y=250)
right_score = Scoreboard(x=70, y=250)

screen.listen()
screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)
screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(start_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() < -320 and ball.distance(left_paddle) < 50 or ball.xcor() > 320 and ball.distance(right_paddle) < 50:
        ball.bounce_x() 
        start_speed *= 0.9


    if ball.xcor() > 380:
        ball.reset_position()
        left_score.update_score()
        start_speed = 0.1
    elif ball.xcor() < -380:
        ball.reset_position()
        right_score.update_score()
        start_speed = 0.1


        
  










screen.exitonclick()
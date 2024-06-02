import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle crosses the road Game")
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()

carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=tim.move_up)
screen.onkey(key="Down", fun=tim.move_down)
screen.onkey(key="Left", fun=tim.move_left)
screen.onkey(key="Right", fun=tim.move_right)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.move()

    if tim.ycor() > 280:
        tim.restart_position()
        scoreboard.update_score()
        carmanager.speed_up()

    for car in carmanager.car_list:
        if tim.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
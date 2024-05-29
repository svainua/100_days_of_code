from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.hideturtle()
tim.pendown()
tim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw(gap_size):
    for i in range(int(360 / gap_size)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)


draw(5)


screen.exitonclick()
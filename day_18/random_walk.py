from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.hideturtle()
tim.pendown()
tim.pensize(15)
tim.speed(10)

angles = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for i in range(200):    
    tim.pencolor(random_color())
    tim.forward(20)
    tim.setheading(random.choice(angles))


screen.exitonclick()
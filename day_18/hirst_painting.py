import random
from turtle import Turtle, Screen
# import colorgram

# colors = colorgram.extract("image.jpg", 30)

# first_color_list = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple  = (r , g, b)
#     first_color_list.append(color_tuple)

color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]

screen = Screen()
screen.colormode(255)

tim = Turtle()


def draw_line(spots_in_line):
    for i in range(spots_in_line):
        tim.dot(size=20)
        tim.color(random.choice(color_list))
        tim.penup()
        tim.forward(50)
        

def draw_picture(rows, columns): 
    tim.hideturtle()
    tim.penup()
    x = -225
    y = -225
    tim.setposition(x=x, y=y)
    tim.speed(0)  
    for d in range(rows):     
        draw_line(columns)
        y += 50 
        tim.setposition(x=x, y=y)


draw_picture(10, 10)









screen.exitonclick()

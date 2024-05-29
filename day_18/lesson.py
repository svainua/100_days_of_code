from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")

tim.pencolor("green")
tim.pendown()


# for i in range(5):
#     tim.forward(200)
#     tim.right(144)

#===========================
# for i in range(4):
#     tim.forward(200)
#     tim.right(90)

#===========================
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

#===========================
# from turtle import *
# color("red", "yellow")
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()    


#===========================
# angle = 360
# rigths = 3

# figures = 6

# while figures > 0:
#     for i in range(rigths):
#         tim.forward(100)
#         tim.right(angle/rigths)
#     rigths += 1
#     figures -= 1

#===========================


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for i in range(3, 11):
#     draw_shape(i)








screen = Screen()
screen.exitonclick()
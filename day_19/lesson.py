from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()

def move_forward():
    tim.forward(10)

def move_back():
    tim.backward(10)

def move_right():
    new_heading = tim.heading() - 10   
    tim.setheading(new_heading)     

def move_left():
    new_heading = tim.heading() + 10   
    tim.setheading(new_heading)  

def clean():
    screen.reset()
    tim.home()        


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clean)

screen.exitonclick()




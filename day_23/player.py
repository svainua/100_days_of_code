from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.setpos(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)    

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(x=new_x, y=self.ycor())    

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(x=new_x, y=self.ycor()) 

    def restart_position(self):
        self.goto(STARTING_POSITION)
        



from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x) -> None:
        super().__init__()
        self.x = x
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.setpos(x=x, y=0)


    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.x, y=new_y)
 

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.x, y=new_y)


from turtle import Turtle

START_POSITION = [(0, 0), (-20,0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)


    def reset(self):
        for seg in self.segments:
            seg.goto(x=1000, y=1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]    


    def extend(self):
        new_segment = self.segments[-1]
        self.add_segment(new_segment.position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0,-1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)   


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)   

    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)       


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)   


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)   


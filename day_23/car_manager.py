import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self) -> None:
        self.car_list = []
        self.create_car()
        self.starting_move_distance = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.setpos(x=290, y=random.randint(-240, 260))
            new_car.setheading(180)
            self.car_list.append(new_car)   


    def move(self):    
        for car in self.car_list:
            new_x = car.xcor() - self.starting_move_distance
            car.goto(x=new_x, y=car.ycor())  


    def speed_up(self):
        self.starting_move_distance += MOVE_INCREMENT    


from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=x, y=y)
        self.write(arg=f"{self.score}", align="center", font=("Arial", 40, "normal"))


    def update_score(self):
        self.clear()
        self.score += 1  
        self.write(arg=f"{self.score}", align="center", font=("Arial", 40, "normal"))





from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(x=-230, y=270)
        self.write(arg=f"Score: {self.score}", align="center", font=(FONT))


    def update_score(self):
        self.clear()
        self.score += 1  
        self.write(arg=f"Score: {self.score}", align="center", font=(FONT))


    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"Game Over", align="center", font=(FONT))
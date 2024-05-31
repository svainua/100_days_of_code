from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self, ) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x=-20, y=280)
        self.color("white")
        self.update_score()


    def update_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()


    def game_over(self):
        self.home()
        self.write(arg="Game Over.", align=ALIGNMENT, font=FONT)



from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")



class ScoreBoard(Turtle):
    def __init__(self, ) -> None:
        super().__init__()
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x=-20, y=280)
        self.color("white")
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score:  {self.score}  High Score:  {self.high_score}" , align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}") 
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}") 
        self.score = 0    
        self.update_scoreboard() 




from turtle import *



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-50, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"SCORE: {self.score}", font=("Verdena", 14))

    def game_over(self):
        self.goto(-70,0)
        self.write(f"Game over!!!", font=("Verdena", 18))


    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
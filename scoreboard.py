from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-190,250)
        self.score1=0
        self.score2=0
        self.update_scoreboard()
        self.hideturtle()
    def plus(self,player):
        if player == "l":
            self.score1 += 1
            self.clear()
            self.update_scoreboard()
        elif player == "r":
            self.score2 += 1
            self.clear()
            self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"Player 1: {self.score1}       Player 2: {self.score2}", move=False, align='left', font=('Arial', 24, 'normal'))
    def end_of_game(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align='center', font=('Arial', 30, 'normal'))
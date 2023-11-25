from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
    def setposition(self,x,y):
        self.penup()
        self.goto(x,y)
    def go_up(self):
        y=self.pos()[1]
        self.setposition(self.pos()[0],y+20)
    def go_down(self):
        y=self.pos()[1]
        self.setposition(self.pos()[0],y-20)






from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.compass="ru"
        self.move_speed=0.1
    def move(self,compass):
        if compass=="ru":
            self.setposition(self.pos()[0]+10,self.pos()[1]+10)
            self.compass="ru"
        elif compass=="rd":
            self.setposition(self.pos()[0]+10,self.pos()[1]-10)
            self.compass="rd"
        elif compass=="lu":
            self.compass = "lu"
            self.setposition(self.pos()[0]-10,self.pos()[1]+10)
        elif compass=="ld":
            self.compass = "ld"
            self.setposition(self.pos()[0]-10,self.pos()[1]-10)

    def wall_colissions(self):
        if self.pos()[1] <= -300 or self.pos()[1] >= 300:
            return True
        else:
            return False

    def wall_bounce(self):
        if self.compass == "ru":
            self.compass = "rd"
        elif self.compass == "rd":
            self.compass = "ru"
        elif self.compass == "lu":
            self.compass = "ld"
        else:
            self.compass = "lu"

    def paddle_collision(self,object):
        if self.distance(object) < 50:
            return True
        else:
            return False

    def paddle_bounce(self):
        if self.compass == "ru":
            self.compass = "lu"
        elif self.compass == "rd":
            self.compass = "ld"
        elif self.compass == "lu":
            self.compass = "ru"
        else:
            self.compass = "rd"
        self.move_speed *= 0.9

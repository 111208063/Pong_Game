from random import *
from turtle import *

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup()

    def paddle1(self):
        self.goto(350,0)
    def paddle2(self):
        self.goto(-350,0)

    def up(self):
        y = self.ycor()+20
        self.goto(self.xcor(), y)
    def down(self):
        x = self.ycor()-20
        self.goto(self.xcor(), x)



class Ball(Turtle):
    def __init__(self):

        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.refresh()
    def refresh(self):
        self.goto(0,0)
        self.xspeed = choice([10,-10])
        self.yspeed = choice([10,-10])

    def move(self):
        x = self.xcor()+self.xspeed
        y = self.ycor()+self.yspeed
        self.goto(x,y)

    def bounce(self):
        self.yspeed = -self.yspeed

    def hit(self):
        self.xspeed = -self.xspeed





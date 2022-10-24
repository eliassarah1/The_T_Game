from turtle import Turtle
from random import randint
import turtle

turtle.register_shape('tissue.gif')


class Tissue(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('tissue.gif')
        self.hideturtle()



    def refresh(self):
        x = randint(-650, 650)
        y = randint(-400, 400)
        self.goto(x, y)

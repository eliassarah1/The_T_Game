from turtle import Turtle
from random import randint
import turtle

turtle.register_shape('food.gif')


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('food.gif')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x = randint(-650, 650)
        y = randint(-400, 400)
        self.goto(x, y)

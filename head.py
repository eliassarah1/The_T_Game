from turtle import Turtle
import turtle

DISTANCE = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

turtle.register_shape('rt.gif')
turtle.register_shape('dt.gif')
turtle.register_shape('ut.gif')
turtle.register_shape('lt.gif')
turtle.register_shape('poop2.gif')
turtle.register_shape('poop.gif')


class Head(Turtle):

    def __init__(self):
        super().__init__()
        self.poops = []
        self.penup()
        self.shape('rt.gif')

    def move(self):
        self.forward(DISTANCE)

    def goup(self):
        self.setheading(UP)
        self.shape('ut.gif')

    def godown(self):
        self.setheading(DOWN)
        self.shape('dt.gif')

    def goleft(self):
        self.setheading(LEFT)
        self.shape('lt.gif')

    def goright(self):
        self.setheading(RIGHT)
        self.shape('rt.gif')

    def pooping(self):
        poop = Turtle()
        poop.penup()
        poop.goto(self.xcor(), self.ycor())
        poop.shape('poop.gif')
        self.poops.append(poop)
        for i in self.poops[0:-1]:
            i.shape('poop2.gif')

    def poopfall(self):
        for i in self.poops[0:-1]:
            i.speed(10)
            i.goto(self.xcor(),self.ycor())
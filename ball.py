from turtle import Turtle
import random
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()

    def serve(self):
        angle = random.randint(0, 360)
        self.setheading(angle)

    def move(self):
        self.forward(10)




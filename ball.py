from turtle import Turtle
import random
import time
player_a_win = 1
player_b_win = 2

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_angle = 0
        self.shape("circle")
        self.color("yellow")
        self.speed("fast")
        self.penup()

    def serve(self):
        self.home()
        self.move_angle = random.randint(0, 45)
        self.setheading(self.move_angle)


    def move(self,paddle_a, paddle_b):
        self.forward(10)
        if self.distance(paddle_b) < 50 and self.xcor() > 320 or self.distance(paddle_a) < 50 and self.xcor() < -320:
            self.move_angle = 180 - self.move_angle
            self.setheading(self.move_angle)

        if self.ycor() > 280 or self.ycor() < -280:
            self.move_angle = 360 - self.move_angle
            self.setheading(self.move_angle)
        if self.xcor() > 400:
            return player_a_win
        elif self.xcor() < -400:
            return player_b_win

        return 0




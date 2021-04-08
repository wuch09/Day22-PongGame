from turtle import Turtle

paddle_a_x = -350
paddle_b_x = 350
paddle_y = 50
paddle_loc = [(-350, 0), (350, 0)]

num_block = 5
paddle_list = []


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.y = self.ycor()
        self.x = self.xcor()


    def move_up(self):
        self.y = self.ycor() + 20
        self.goto(self.x, self.y)


    def move_down(self):
        self.y = self.ycor() -20
        self.goto(self.x, self.y)




    def head_pos(self):
        pass

    def tail_pos(self):
        pass

    def check_boundary(self):
        pass


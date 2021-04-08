from turtle import Turtle

paddle_a_x = -350
paddle_b_x = 350
paddle_y = 50
paddle_loc = [(-350, 0), (350, 0)]

num_block = 5
paddle_list = []


class Paddle(Turtle):
    def __init__(self,player):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        if player == 0:
            self.goto(paddle_a_x, 0)
        elif player ==1:
            self.goto(paddle_b_x, 0)


    def move_up(self):
        pos_y = self.ycor() + 20
        pos_x = self.xcor()
        self.goto(pos_x, pos_y)


    def move_down(self):
        pos_y = self.ycor() -20
        pos_x = self.xcor()
        self.goto(pos_x, pos_y)




    def head_pos(self):
        pass

    def tail_pos(self):
        pass

    def check_boundary(self):
        pass


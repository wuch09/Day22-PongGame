from score_board import ScoreBoard
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
import time
player_a = 0
player_b = 1
key_list = [("w", "s"), ("Up", "Down")]
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("my Pong Game")
screen.tracer(0)


player_a_score = ScoreBoard(player_a)
player_b_score = ScoreBoard(player_b)
player_b_score.update_score()
player_a_score.update_score()

player_a_paddle = Paddle((-350,0))
player_b_paddle = Paddle((350,0))
ball = Ball()
ball.serve()
screen.update()

#screen.update()
# Todo #1 on key listen
screen.listen()
screen.onkey(player_a_paddle.move_up, "w")
screen.onkey(player_a_paddle.move_down, "x")
screen.onkey(player_b_paddle.move_up, "Up")
screen.onkey(player_b_paddle.move_down, "Down")

game_is_on = True
while game_is_on:
    ball.move()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()

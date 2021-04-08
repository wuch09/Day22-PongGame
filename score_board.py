from turtle import Turtle

players_position = [(-100, 240), (60, 240)]
SCORE_FONT= GAME_OVER_FONT = ("Times", 40, "bold")


class ScoreBoard(Turtle):
    def __init__(self, user):
        super().__init__()
        self.position = players_position[user]
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(self.position)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(str(self.score), align="center", font=SCORE_FONT)

    def increase_score(self):
        self.score += 1





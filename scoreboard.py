from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('black')

    def initialize_scoreboard(self):
        self.clear()
        self.goto(-230,270)
        self.write(f"Score: {self.score}", align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.initialize_scoreboard()

    def game_over_sequence(self):
        self.goto(0,0)
        self.write(f"     GAME OVER     \n  Your score is {self.score}\n  Press R to reset   ", align='center', font=FONT)


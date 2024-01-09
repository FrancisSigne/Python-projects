from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.color("white")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


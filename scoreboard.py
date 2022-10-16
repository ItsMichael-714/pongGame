from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self, position, player):
        super().__init__()
        self.score = 0
        self.player = player
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_scoreboard(self.player)

    def update_scoreboard(self, player):
        self.clear()
        self.write(f"{player}: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self, player):
        self.score += 1
        self.update_scoreboard(player)

    def game_over(self, player):
        self.goto(0, 0)
        self.write(f"GAME OVER. {player} Wins!", align=ALIGN, font=FONT)


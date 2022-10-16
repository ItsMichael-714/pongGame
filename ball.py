import turtle
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize()
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move_ball(self):
        y_cor = self.ycor() + self.y_move
        x_cor = self.xcor() + self.x_move
        self.goto(x_cor, y_cor)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)


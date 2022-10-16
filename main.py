from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=900, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
time.sleep(.1)

l_player = screen.textinput("Left Player", "Enter left player's name: ")
r_player = screen.textinput("Right Player", "Enter right player's name: ")
r_paddle = Paddle((420, 0))
l_paddle = Paddle((-420, 0))
ball = Ball()
l_scoreboard = Scoreboard((-400, 275), l_player)
r_scoreboard = Scoreboard((385, 275), r_player)

play_to_points = int(screen.textinput("First to how many points?", "The first player to reach how many points wins? "))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_dn, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_dn, "s")

game_on = True
while game_on:
    time.sleep(.1)
    screen.update()
    ball.move_ball()

    # detect collision with top and bottom walls for bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 400 or ball.distance(l_paddle) < 50 and ball.xcor() < -400:
        ball.paddle_bounce()

    # detect missed paddle and award points

    if ball.xcor() > 422:  # when left player scores
        time.sleep(1)
        ball.reset_position()
        ball.paddle_bounce()  # changes the direction so the other player gets first serve
        l_scoreboard.increase_score(l_player)
        l_scoreboard.update_scoreboard(l_player)
    elif ball.xcor() < -422:  # when right player scores
        time.sleep(1)
        ball.reset_position()
        ball.paddle_bounce()  # changes the direction so the other player gets first serve
        r_scoreboard.increase_score(r_player)
        r_scoreboard.update_scoreboard(r_player)

    if r_scoreboard.score == play_to_points:
        print(r_scoreboard.score)
        r_scoreboard.game_over(r_player)
        game_on = False
    elif l_scoreboard.score == play_to_points:
        print(l_scoreboard.score)
        l_scoreboard.game_over(l_player)
        game_on = False

screen.exitonclick()

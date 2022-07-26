from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
screen.listen()

right_paddle = Paddle(350, 0)
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

left_paddle = Paddle(-350, 0)
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()

    time.sleep(ball.move_speed)
    ball.move()

    # Wall collision detection
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y_axis()

    # Paddles collision detection
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50:
        ball.bounce_x_axis()

    if ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x_axis()

    # Right side out-of-bounds detection
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.point_for_left()
        scoreboard.update_scoreboard()

    # Left side out-of-bounds detection
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.point_for_right()
        scoreboard.update_scoreboard()

    if scoreboard.left_score == 10 or scoreboard.right_score == 10:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()

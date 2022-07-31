from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

food = Food()
score = Scoreboard()
score.color("white")
score.hideturtle()

# Enable keyboard listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Food collision detection
    if snake.head.distance(food) < 15:
        score.gain_a_point()
        food.refresh()
        snake.extend_body()

    # Walls collision detection
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_scoreboard()
        snake.reset_snake()

    # Tail collision detection
    for segment in snake.body_segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()

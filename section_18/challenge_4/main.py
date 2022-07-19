from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.speed("slowest")
colormode(255)
tim.width(15)

for i in range(25):
    tim.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    number_of_turns = random.randint(0, 3)
    turn_direction = random.choice(["left", "right"])
    for j in range(number_of_turns):
        if turn_direction == "left":
            tim.left(90)
        else:
            tim.right(90)
    tim.forward(50)

screen = Screen()
screen.exitonclick()

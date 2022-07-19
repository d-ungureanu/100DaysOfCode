from turtle import Turtle, Screen, colormode
from random import randint

tim = Turtle()
colormode(255)
for i in range(3, 11):
    tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    for j in range(i):
        tim.forward(100)
        tim.right(360 / i)

screen = Screen()
screen.exitonclick()

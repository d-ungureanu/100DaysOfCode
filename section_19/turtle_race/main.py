from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -70, -40, -10, 20, 50]
turtles_list = []

for turtle_index in range(6):
    racer = Turtle(shape="turtle")
    racer.penup()
    racer.color(colours[turtle_index])
    racer.goto(x=-230, y=y_position[turtle_index])
    turtles_list.append(racer)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

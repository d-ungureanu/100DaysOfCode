# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("dots.jpg", 30)
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     rgb_colors.append((red, green, blue))
# print(rgb_colors)
import turtle as turtle_module
import random

colors_list = [(223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159), (209, 161, 111),
               (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43), (195, 130, 169),
               (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87), (193, 187, 46),
               (240, 204, 2), (1, 102, 119), (19, 22, 21), (50, 150, 109), (172, 212, 172), (118, 36, 34),
               (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210)]

new_turtle = turtle_module.Turtle()
turtle_module.colormode(255)
new_turtle.hideturtle()
y = -200
for j in range(10):
    new_turtle.penup()
    new_turtle.goto(-200, y)
    for i in range(10):
        new_turtle.pencolor(random.choice(colors_list))
        new_turtle.penup()
        new_turtle.forward(50)
        new_turtle.dot(20)
    y += 50


screen = turtle_module.Screen()
screen.exitonclick()

# from turtle import Turtle, Screen
#
# # import another_module
# # print(another_module.another_variable)
#
# mimmy = Turtle()
# print(mimmy)
# mimmy.shape("turtle")
# mimmy.color("blue")
# print(mimmy.pos())
# mimmy.forward(100.00)
# print(mimmy.pos())
# mimmy.left(90)
# mimmy.forward(100.00)
# print(mimmy.pos())
# mimmy.left(90)
# mimmy.forward(100.00)
# print(mimmy.pos())
# mimmy.left(90)
# mimmy.forward(100.00)
# print(mimmy.pos())
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = "l"
print(table)

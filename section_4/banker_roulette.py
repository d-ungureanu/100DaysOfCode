import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
random_index = random.randint(0, len(names) - 1)
print(f"{names[random_index]} is going to buy the meal today!")

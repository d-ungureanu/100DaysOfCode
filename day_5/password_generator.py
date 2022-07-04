# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = []
letters_list = []
for i in range(0, nr_letters):
    letters_list.append(letters[random.randint(0, 52)])
password.extend(letters_list)

symbols_list = []
for i in range(0, nr_symbols):
    symbols_list.append(symbols[random.randint(0, 8)])
password.extend(symbols_list)

numbers_list = []
for i in range(0, nr_numbers):
    numbers_list.append(numbers[random.randint(0, 9)])
password.extend(numbers_list)
easy_password = "".join(password)
print(easy_password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password_list = password.copy()
random.shuffle(hard_password_list)
hard_password = "".join(hard_password_list)
print(hard_password)

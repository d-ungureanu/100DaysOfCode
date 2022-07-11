import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
chosen_number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    number_of_tries = 10
elif difficulty == "hard":
    number_of_tries = 5
print(f"You have {number_of_tries} attempts remaining to guess the number.")
while number_of_tries > 0:
    guess = int(input("Make a guess: "))
    if guess == chosen_number:
        print(f"You got it! The answer was {chosen_number}.")
    elif guess < chosen_number:
        print("Too low.")
        number_of_tries -= 1
        print(f"You have {number_of_tries} attempts remaining to guess the number.")
    elif guess > chosen_number:
        print("Too high.")
        number_of_tries -= 1
        print(f"You have {number_of_tries} attempts remaining to guess the number.")
print("You've run out of guesses, you lose.")

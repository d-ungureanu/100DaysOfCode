import random
from art import logo

EASY_MODE = 10
HARD_MODE = 5


def choose_difficulty():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_level == "easy":
        return EASY_MODE
    elif difficulty_level == "hard":
        return HARD_MODE


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def guessing_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    chosen_number = random.randint(1, 100)

    number_of_guesses = choose_difficulty()
    user_guess = 0
    while user_guess != chosen_number:
        print(f"You have {number_of_guesses} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        number_of_guesses = check_answer(user_guess, chosen_number, number_of_guesses)

        if number_of_guesses == 0:
            print("You've run out of guesses, you lose.")
            return
        elif user_guess != chosen_number:
            print("Guess again")


guessing_game()

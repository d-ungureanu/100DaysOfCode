import os
import random
from game_data import data
from art import logo, vs


def clear():
    os.system("cls")


def pick_celebrity(list_of_celebrities):
    random_index = random.randint(0, len(list_of_celebrities) - 1)
    celebrity = list_of_celebrities[random_index]
    return celebrity


def compare_followers(celeb_a, celeb_b):
    score = 0
    keep_playing = True
    while keep_playing:
        followers_a = celeb_a["follower_count"]
        followers_b = celeb_b["follower_count"]
        print(f"Compare A: {celeb_a['name']}, a {celeb_a['description']}, from {celeb_a['country']}.")
        print(vs)
        print(f"Compare B: {celeb_b['name']}, a {celeb_b['description']}, from {celeb_b['country']}.")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        higher_count = ""
        if followers_a > followers_b:
            higher_count = "a"
        elif followers_b > followers_a:
            higher_count = "b"
        if choice == higher_count:
            score += 1
            print(f"You're right! Current score: {score}.")
            celeb_a = celeb_b
            celeb_b = pick_celebrity(data)
        else:
            keep_playing = False
            print(f"Sorry, that's wrong. Final score: {score}")


def higher_lower():
    print(logo)
    first_celeb = pick_celebrity(data)
    second_celeb = pick_celebrity(data)
    compare_followers(first_celeb, second_celeb)


higher_lower()

import random
import os
from art import logo


def deal_card():
    """Returns value of a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(list_of_cards):
    """Calculates the sum of cards' values in a cards list."""
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0
    if sum(list_of_cards) > 21 and (11 in list_of_cards):
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return sum(list_of_cards)


def compare_scores(p_score, c_score):
    if p_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You lose, opponent has Blackjack"
    elif p_score == 0:
        return "You win with Blackjack"
    elif p_score > 21:
        return "You lose, you went over 21"
    elif c_score > 21:
        return "You win, opponent went over 21"
    elif p_score > c_score:
        return "You win"
    else:
        return "You lose"


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def play_blackjack():
    print(logo)
    player_cards = []
    computer_cards = []
    stop_playing = False

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not stop_playing:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {player_cards}, current score: {player_score}")
        print(f"    Computer's first card: {computer_cards[0]}")
        if player_score == 0 or computer_score == 0 or player_score > 21:
            stop_playing = True
        else:
            player_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if player_deal == "y":
                player_cards.append(deal_card())
            else:
                stop_playing = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {player_cards}, final score: {player_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(player_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    clear_screen()
    play_blackjack()

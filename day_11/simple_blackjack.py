import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    player_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if player_choice == "n":
        exit()

    print(logo)
    player_cards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
    player_score = sum(player_cards)
    print(f"    Your cards: {player_cards}, current score: {player_score}")

    computer_cards = [cards[random.randint(0, 12)]]
    computer_score = sum(computer_cards)
    print(f"    Computer's first card: {computer_cards[0]}")

    while player_score < 21:
        ask_for_cards = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if ask_for_cards == "y":
            player_cards.append(cards[random.randint(0, 12)])
            if (11 in player_cards) and (sum(player_cards) > 21):
                player_score = sum(player_cards) - 10
            else:
                player_score = sum(player_cards)
            print(f"    Your cards: {player_cards}, current score: {player_score}")
            print(f"    Computer's first card: {computer_cards[0]}")
        elif ask_for_cards == "n":
            print(f"    Your final hand: {player_cards}, final score: {player_score}")
            while computer_score < 17:
                computer_cards.append(cards[random.randint(0, 12)])
                if (11 in computer_cards) and (sum(computer_cards) > 21):
                    computer_score = sum(computer_cards) - 10
                else:
                    computer_score = sum(computer_cards)
        break
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

    if (player_score == computer_score) or (player_score > 21 and computer_score > 21):
        print("It's a draw")
    elif (player_score < 22) and (computer_score < 22):
        if player_score > computer_score:
            print("You win")
        else:
            print("You lose")
    blackjack()


blackjack()

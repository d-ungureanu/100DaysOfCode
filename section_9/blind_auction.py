from art import logo
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print(logo)
print("Welcome to the secret auction program.")
bidders_list = {}
while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders_list[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if choice == "no":
        break
    clear()
max_bid = 0
winning_name = ""
for bidder in bidders_list:
    if bidders_list[bidder] > max_bid:
        max_bid = bidders_list[bidder]
        winning_name = bidder
print(f"The winner is {winning_name} with a bid of ${max_bid}.")

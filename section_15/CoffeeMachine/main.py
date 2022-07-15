from data import MENU, resources


def print_report():
    print(f"{'Water'.ljust(8)}: {resources['water']}ml")
    print(f"{'Milk'.ljust(8)}: {resources['milk']}ml")
    print(f"{'Coffee'.ljust(8)}: {resources['coffee']}ml")
    print(f"{'Money'.ljust(8)}: ${resources['money']}")


def check_resources(order_ingredients):
    """Returns True if there are enough resources for the ordered drink."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Return the total calculated from the coins inserted into the coffee machine"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    user_total = round(0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies, 2)
    return user_total


def enough_money_for_drink(money_received, drink_cost):
    """Return True if payment is accepted, or False if money insufficient"""
    if money_received >= drink_cost:
        resources["money"] += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_drink(drink_name, order_ingredients):
    """Deduct order ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


def start_coffee_machine():
    machine_on = True
    while machine_on:
        user_choice = input("   What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "off":
            machine_on = False
        elif user_choice == "report":
            print_report()
        elif user_choice in ["espresso", "latte", "cappuccino"]:
            drink = MENU[user_choice]
            if check_resources(drink["ingredients"]):
                user_payment = process_coins()
                if enough_money_for_drink(user_payment, drink["cost"]):
                    make_drink(user_choice, drink["ingredients"])



        else:
            print("Option not on the menu.")


start_coffee_machine()

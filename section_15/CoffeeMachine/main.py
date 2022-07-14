from data import MENU, resources


def print_report():
    print(f"{'Water'.ljust(8)}: {resources['water']}ml")
    print(f"{'Milk'.ljust(8)}: {resources['milk']}ml")
    print(f"{'Coffee'.ljust(8)}: {resources['coffee']}ml")
    print(f"{'Money'.ljust(8)}: ${resources['money']}")


def check_resources(drink_name, resources_available):
    required_water = MENU[drink_name]["ingredients"]["water"]
    required_coffee = MENU[drink_name]["ingredients"]["coffee"]
    required_milk = MENU[drink_name]["ingredients"]["milk"]
    available_water = resources_available["water"]
    available_coffee = resources_available["coffee"]
    available_milk = resources_available["milk"]
    if required_water > available_water:
        print("Sorry there is not enough water.")
        return False
    if required_coffee > available_coffee:
        print("Sorry there is not enough coffee.")
        return False
    if required_milk > available_milk:
        print("Sorry there is not enough milk.")
        return False
    return True


def check_coins(chosen_drink, drinks_menu):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    user_total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    drink_price = drinks_menu[chosen_drink]["cost"]
    if user_total < drink_price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = user_total - drink_price
        print(f"Here is ${change} in change.")
        resources["money"] += drink_price
    return True


def start_coffee_machine():
    machine_on = True
    while machine_on:
        user_choice = input("   What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "off":
            machine_on = False
        elif user_choice == "report":
            print_report()
        elif user_choice in ["espresso", "latte", "cappuccino"]:
            if check_resources(user_choice, resources):
                if check_coins(user_choice, MENU):
                    print(f"Here is your {user_choice} ☕. Enjoy!")
        else:
            print("Option not on the menu.")


start_coffee_machine()

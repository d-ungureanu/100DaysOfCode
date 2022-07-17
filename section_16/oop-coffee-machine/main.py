from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_handler = MoneyMachine()
menu = Menu()

machine_on = True

while machine_on:
    drinks_options = menu.get_items()
    user_choice = input(f"   What would you like? ({drinks_options}): ").lower()
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        coffee_machine.report()
        money_handler.report()
    elif user_choice in ["espresso", "latte", "cappuccino"]:
        chosen_drink = menu.find_drink(user_choice)

        if coffee_machine.is_resource_sufficient(chosen_drink):
            if money_handler.make_payment(chosen_drink.cost):
                coffee_machine.make_coffee(chosen_drink)

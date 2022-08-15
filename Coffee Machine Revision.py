from _Data import MENU
from _Data import resources


def drink_choice():
    # TODO Make sure only correct input is entered
    choice = ""
    incorrect_input = True
    while incorrect_input:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice != "latte" \
                and choice != "espresso" \
                and choice != "cappuccino" \
                and choice != "report" \
                and choice != "off":
            choice = input("Please enter either espresso, latter or cappuccino as your drink of choice: ")
        else:
            incorrect_input = False
    return choice


profit = 0


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def sufficient_resources(drink):
    for key in resources:
        if resources[key] < MENU[drink]["ingredients"][key]:
            print(f"There's not enough {key}.")
            coffee_machine()


def verify_transaction(drink):
    total_cash = float(input("Enter quarters: ")) * 0.25
    total_cash += float(input("Enter dimes: ")) * 0.1
    total_cash += float(input("Enter quarters: ")) * 0.25
    total_cash += float(input("Enter quarters: ")) * 0.25
    # print(total_cash)
    drink_cost = MENU[drink]["cost"]
    if total_cash < drink_cost:
        print("Sorry that's not enough money. Money refunded")
        coffee_machine()
    else:
        global profit
        profit += drink_cost
        change = total_cash - drink_cost
        print(f"Here's your change: ${change}")


def make_coffee(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    print(f"Here's your {drink}")


def coffee_machine():
    coffee_machine_on = True
    while coffee_machine_on:
        # TODO Print report of remaining resources and also turn machine off
        choice = drink_choice()
        if choice == "report":
            print_report()
        elif choice == "off":
            coffee_machine_on = False
        else:
            sufficient_resources(choice)
            # print(f"Resources are sufficient to make {choice}")
# TODO Process coins
            verify_transaction(choice)
#             total_cash = verify_transaction(choice)
            # print(total_cash)
            make_coffee(choice)


coffee_machine()






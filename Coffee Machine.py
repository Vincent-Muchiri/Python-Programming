# Make three hot flavours

import _Data
resources = _Data.resources
# print(resources)

#TODO Add money to the resources dictionary
resources["money"] = 0


def coffee_machine():
    machine_ON = True
    while machine_ON:
        # TODO Take an order
        response = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # TODO Make sure the right response is entered
        wrong_response = True
        while wrong_response:
            if response != "espresso" and response != "latte" and response != "capuccino" and response != "report" and response != "off":
                response = input("Please enter the right response.(espresso/latte/capuccino): ").lower()
            else:
                wrong_response = False

        # TODO Turn the machine off
        if response == "off":
            machine_ON = False

        # TODO Print report of remaining ingredients: water, milk, coffee
        elif response == "report":
            print(f" Water: {resources['water']}ml")
            print(f" Milk: {resources['milk']}ml")
            print(f" Coffee: {resources['coffee']}gm")
            print(f" Money: ${resources['money']}")
            coffee_machine()
        else:
            menu = _Data.MENU[response]
            # print(menu)
            ingredients = menu["ingredients"]
            # print(ingredients)

            # TODO Check whether the resources are sufficient for making the drink
            # insufficient_resources = True
            # while insufficient_resources:
            #     # print(ingredients)
            #     # print(resources["water"])
            #     # print(ingredients["water"])
            #     if resources["water"] < ingredients["water"]:
            #         print("Sorry there is not enough water.")
            #         coffee_machine()
            #     elif resources["milk"] < ingredients["milk"]:
            #         print("Sorry there is not enough milk.")
            #         coffee_machine()
            #     elif resources["coffee"] < ingredients["coffee"]:
            #         print("Sorry theres not enough coffee")
            #         coffee_machine()
            #     else:
            #         insufficient_resources = False

            for item in ingredients:
                if resources[item] < ingredients[item]:
                    print(f"Sorry there is not enough {item}.")
                    coffee_machine()

        print("Please insert coins.")
        total_amount = int(input("How many quarters? ")) * 0.25
        total_amount += int(input("How many dimes? ")) * 0.10
        total_amount += int(input("How many nickels? ")) * 0.05
        total_amount += int(input("How many pennies? ")) * 0.01

        # TODO Calculate total amount of coins inserted
        # total_amount = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
        # print(total_amount)
        # TODO Check whether enough money has been inserted otherwise refund the money
        if total_amount < menu["cost"]:
            print("Sorry that's not enough money. Money refunded")
        else:
            # TODO Make the drink and update the resources
            # print(resources)
            # print(ingredients)
            resources["water"] -= ingredients["water"]
            resources["milk"] -= ingredients["milk"]
            resources["coffee"] -= ingredients["coffee"]

            #TODO Add the drink amount to the resources
            resources["money"] += menu["cost"]

            # print(resources)

            print("Here's your "+response+". Enjoy!")
        # TODO Give change if necessary
        if total_amount > menu["cost"]:
            change = total_amount - menu["cost"]
            print(f"Here is ${change} in change.")


coffee_machine()







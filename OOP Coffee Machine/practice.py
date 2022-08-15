from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO Create all the objects from the classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_Machine = MoneyMachine()

machine_on = True
while machine_on:
    # TODO Prompt user to enter drink
    response = input(f"What would you like? ({menu.get_items()}): ").lower()

    # TODO Turn off the coffee machine by entering "off"
    if response == "off":
        machine_on = False
    #TODO Print report
    elif response == "report":
        print(coffee_maker.report())
    # elif response != "latte" and response != "espresso" and response != "cappuccino":
    #     response = input(f"Wrong entry. Please choose either {menu.get_items()}: ")
    else:
        # TODO Check whether resources are sufficient to make the drink
        drink = menu.find_drink(response)
        # print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            # print("Resources enough")
            #TODO Process coins
            order_cost = drink.cost
            # print(order_cost)
            # print(type(order_cost))
            if money_Machine.make_payment(order_cost):
                coffee_maker.make_coffee(drink)
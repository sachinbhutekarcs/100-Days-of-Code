import sys
# espresso latte & cappuccino
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
enough_resources = True


# define a function to generate the report
def report():
    print(f"Water 💧: {resources['water']}")
    print(f"Milk 🥛: {resources['milk']}")
    print(f"Coffee 🍫: {resources['coffee']}")
    print(f"Money 💸: ${money}")


# define a function to check resources
def check_resources(name):
    global enough_resources, money
    if resources['water'] < MENU[name]["ingredients"]["water"]:
        print(f"Sorry☹ there is not enough water💧.")
        sys.exit()
    elif name != "espresso" and resources['milk'] < MENU[name]["ingredients"]['milk']:
        print(f"Sorry☹ there is not enough milk🥛.")
        sys.exit()
    elif resources['coffee'] < MENU[name]["ingredients"]['coffee']:
        print(f"Sorry☹ there is not enough coffee🍫.")
        sys.exit()
    else:
        enough_resources = True


# define a function to take money from customer, check if it's sufficient or not and return change if money is extra
def pay_bill(name):
    global money, enough_resources
    coins = {"pennies": 0, "nickles": 0, "dimes": 0, "quarters": 0}
    print("Enter the coins")
    for i in coins:
        coins[i] = int(input(f"{i}💰: "))
    bill = coins["pennies"]*0.01 + coins["nickles"] * \
        0.05 + coins["dimes"]*0.1 + coins["quarters"]*0.25
    if bill < MENU[name]["cost"]:
        print(f"Sorry☹ that is not enough money💸. Money Refunded")
        enough_resources = False
    else:
        money = MENU[name]['cost']
        print(
            f"“Here is ${round(bill - MENU[name]['cost'], 2)}dollars💸 in change.")


# define a function  to make the coffee and update resources and money
def make_a_coffee(name):
    resources["water"] -= MENU[name]["ingredients"]["water"]
    if name != "espresso":
        resources["milk"] -= MENU[name]["ingredients"]["milk"]
    resources["coffee"] -= MENU[name]["ingredients"]["coffee"]
    print(f"Here is your {name} ☕, enjoy!")


def coffee_machine():
    global enough_resources
    while enough_resources:
        user_input = input(
            "What would you like to have ☕? (espresso/latte/cappuccino): ").lower()
        if user_input == "off":
            print("Switching off....Done")
            sys.exit()
        elif user_input == "report":
            report()
        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            check_resources(user_input)
            pay_bill(user_input)
            make_a_coffee(user_input)
        else:
            print("Invalid Input🚫")


coffee_machine()

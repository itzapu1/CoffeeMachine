from coffee_resources import MENU, resources

menu = MENU
current_resources = resources


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def print_report(resources, money):
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Moneys: {money}")
    pass


def check_resources(user_order):
    """Takes in the user order and checks if there are enough resources to fulfill the order. It returns a boolean"""
    ingredients = MENU[user_order]['ingredients']
    for ingredient in ingredients:
        value = current_resources[ingredient] - ingredients[ingredient]
        if value < 0:
            print(f"Sorry, there is not enough {ingredient}")
            return False
        else:
            # print(f"Good Amount")
            current_resources[ingredient] = value
    return True


def check_transaction(user_order, inserted_coins):
    item_cost = MENU[user_order]['cost']
    if inserted_coins >= item_cost:
        # money += inserted_coins
        change_made = inserted_coins - item_cost
        print(f"Here is ${change_made} in change")
        return item_cost
    else:
        print("Sorry thats not enough money. Money refunded")
        return 0


def process_coins():
    """Asks for user to input coins and returns the total amount as float"""
    num_of_quarters = int(input("How many quarters?: "))
    num_of_dimes = int(input("How many dimes?: "))
    num_of_nickles = int(input("How many nickles?: "))
    num_of_pennies = int(input("How many pennies?: "))

    total = round(num_of_quarters * 0.25 + num_of_dimes * 0.10 + num_of_nickles * 0.05 + num_of_pennies * 0.01, 3)
    #print(f"Total amount provided: ${total}")
    return total


def make_coffee():
    print("Making Coffee now")
    pass


def run():
    is_running = True
    money = 0
    while is_running:
        user_order = input("What would you like? (espresso/latte/cappuccino) ").lower()
        if user_order == "off":
            is_running = False
        elif user_order == "report":
            print_report(current_resources, money)
        else:
            if check_resources(user_order):
                inserted_coins = process_coins()
                # print_report(current_resources, money)
                storage = check_transaction(user_order, inserted_coins)
                print("--- break 2 ---")
                if storage == 0:
                    print("--- break ----")
                    # print_report(current_resources, money)
                else:
                    money += storage
                    make_coffee()
                    print("--- break ----")


if __name__ == '__main__':
    run()

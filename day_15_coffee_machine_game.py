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

def make_coffee(drink_name, oder_ingredients):
    for items in oder_ingredients:
        resources[items] -= oder_ingredients[items]
    print(f"Here your drink {drink_name}☕ enjoy!")



def check_transaction(money,drink_cost):
    if money >= drink_cost:
        global price
        change = round(money - drink_cost,2)
        print(f"Here your change ${change}")
        price += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")






def process_coins():
    """This function retuens the total value of the money"""
    print("Please insert coins:")
    total =int(input("how many quarters:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total +=int(input("how many nickles?:")) * 0.05
    total +=int(input("how many pennies?:")) *0.01
    return total
def check_resources(order_ingredients):
    for items in order_ingredients:
       if order_ingredients[items] >= resources[items]:
           print("Sorry there is not enough water. ")
           return False
    return True

machine_turn_on = True
price = 0
while machine_turn_on:
    choice = input("“What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        machine_turn_on = False
    elif choice == "report":
        print(f"total resources are:\nwater:  {resources['water']}\nmilk: {resources['milk']}\ncoffee: {resources['coffee']}\nMoney: {price}. ")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if check_transaction(payment,drink["cost"]):
                make_coffee(choice,drink['ingredients'])


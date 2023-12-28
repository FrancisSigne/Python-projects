drinks = [
    {"drink": "Espresso", "Water": 50, "Milk": 0, "Coffee": 50, "Cost": 1.5},
    {"drink": "Latte", "Water": 100, "Milk": 150, "Coffee": 100, "Cost": 2.5},
    {"drink": "Cappuccino", "Water": 150, "Milk": 100, "Coffee": 200, "Cost": 4}
]

machine = {"Water": 500, "Milk": 500, "Coffee": 500}

money = 0
report = f"Water: {machine['Water']} ml\nMilk: {machine['Milk']} ml\nCoffee: {machine['Coffee']} g\nMoney: ${money}"


def find_index(choice):
    """Find the dictionary index of the drink choice"""
    for num in range(3):
        if drinks[num]['drink'] == choice:
            return num


def check_resources(index):
    """Loop through the coffee machine resources and compare them to the drink requirement"""
    for resource in machine:
        if (machine[resource]) < drinks[index][resource]:
            return resource
    return 1


def process_coins():
    """Calculate how much money was put into the machine"""
    print("Please insert coin.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickel = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))
    paid = (quarters * 0.25) + (dimes * 0.10) + (nickel * 0.05) + (pennies * 0.01)
    return paid


def transaction(index, payment):
    """Determinate whether or not the money inserted is enough for the drink"""
    if drinks[index]['Cost'] < payment:
        rest = payment - drinks[index]['Cost']
        print(f"Here is ${rest} dollars in change.")
        return drinks[index]['Cost']
    elif drinks[index]['Cost'] == payment:
        return drinks[index]['Cost']
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return 0


def coffee_machine():
    """Get you a coffee of your choice"""
    keep_ordering = True
    global money, report

    while keep_ordering:
        order = input("What would you like? (espresso/latte/cappuccino): ").capitalize()
        drink_index = find_index(choice=order)

        if order == "Report":
            print(report)
        elif order == "Off":
            keep_ordering = False
            return
        else:
            answer = check_resources(index=drink_index)
            if answer == 1:
                pay = process_coins()
                is_enough = transaction(index=drink_index, payment=pay)
                if is_enough != 0:
                    print(f"Here is your {order} ☕")
                    money += is_enough
                    for item in machine:
                        machine[item] -= drinks[drink_index][item]
                    report = f"Water: {machine['Water']}\nMilk: {machine['Milk']}\nCoffee: {machine['Coffee']}\nMoney: {money}"
            else:
                print(f"Sorry there is not enough {answer}")


coffee_machine()


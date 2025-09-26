import menu_and_resources


#TODO: 9 Create variables for everything required
resources = menu_and_resources.resources
water_level = menu_and_resources.resources["water"]
milk_level = menu_and_resources. resources["milk"]
coffee_amount = menu_and_resources.resources["coffee"]
menu = menu_and_resources.MENU
machine_money = 0
penny = menu_and_resources.coins["penny"]
nickel = menu_and_resources.coins["nickel"]
dime = menu_and_resources.coins["dime"]
quarter = menu_and_resources.coins["quarter"]



# TODO: 2 Ask user what they like (espresso/latte/cappuccino
def user_input(decision):
    # make_choice = input("What would you like? Espresso / Latte / Cappuccino: ").lower()
    return decision

def user_order(request, drinks):
    if request == "latte":
        order_water_latte = drinks["latte"]["ingredients"]["water"]
        order_milk_latte = drinks["latte"]["ingredients"]["milk"]
        order_coffee_latte = drinks["latte"]["ingredients"]["coffee"]
        order_cost_latte = drinks["latte"]["cost"]
        ingredients = {
            "name" : request,
            "water" : order_water_latte,
            "milk" : order_milk_latte,
            "coffee" : order_coffee_latte,
            "cost" : order_cost_latte,
        }
        return ingredients
    elif request == "espresso":
        order_water_espresso = drinks["espresso"]["ingredients"]["water"]
        order_milk_espresso = 0
        order_coffee_espresso = drinks["espresso"]["ingredients"]["coffee"]
        order_cost_espresso = drinks["espresso"]["cost"]
        ingredients = {
            "name": request,
            "water": order_water_espresso,
            "milk" : order_milk_espresso,
            "coffee": order_coffee_espresso,
            "cost": order_cost_espresso,
        }
        return ingredients
    elif request == "cappuccino":
        order_water_cappuccino = drinks["cappuccino"]["ingredients"]["water"]
        order_milk_cappuccino = drinks["cappuccino"]["ingredients"]["milk"]
        order_coffee_cappuccino = drinks["cappuccino"]["ingredients"]["coffee"]
        order_cost_cappuccino = drinks["cappuccino"]["cost"]
        ingredients = {
            "name": request,
            "water": order_water_cappuccino,
            "milk": order_milk_cappuccino,
            "coffee": order_coffee_cappuccino,
            "cost": order_cost_cappuccino,
        }
        return ingredients
    else:
        return None


# TODO: 1 Print a report of all the resources
def report(water, milk, coffee, cash):
        return f"Water: {water}\n Milk: {milk}\n Coffee: {coffee}\n Money: {cash}"



def report_off(user):
    if user == "report":
        return "True"
    elif user == "off":
        return "False"
    else:
        return None


# TODO: 3 Turn off the machine using "off" to the prompt
# def off(request):
#     if request == "off":
#         return False
#     return None


# TODO: 7 Make coffee after transaction is successful.




# TODO: 8 Deduct from resources after each coffee.
def make_coffee(choice1, request, water, milk, coffee):
    order_water = choice1["water"]
    order_milk = choice1["milk"]
    order_coffee = choice1["coffee"]
    response = ""
    brewing = True
    while brewing:
        water -= order_water
        milk -= order_milk
        coffee -= order_coffee
        response = f"Here is your {request}. Enjoy"
        brewing = False

    return water, milk, coffee, response






# TODO: 4 Check that the resources are sufficient when user chooses a drink
def check_resources(request, water, milk, coffee):
    name= request["name"]
    espresso_water = request["water"]
    espresso_milk = request["milk"]
    espresso_coffee = request["coffee"]
    latte_water = request["water"]
    latte_milk = request["milk"]
    latte_coffee = request["coffee"]
    cappuccino_water = request["water"]
    cappuccino_milk = request["milk"]
    cappuccino_coffee = request["coffee"]
    if name == "espresso":
        if water >= espresso_water:
            if milk >= espresso_milk:
                if coffee >= espresso_coffee:
                    return "Coffee"
                else:
                    return "No Coffee"
            else:
                return "No coffee"
        else:
            return "No Coffee"
    elif name == "latte":
        if water >= latte_water:
            if milk >= latte_milk:
                if coffee >= latte_coffee:
                    return "Coffee"
                else:
                    return "No Coffee"

            else:
                return "No Coffee"
        else:
            return None
    elif name == "cappuccino":
        if water >= cappuccino_water:
            if milk >= cappuccino_milk:
                if coffee >= cappuccino_coffee:
                    return "Coffee"
                else:
                    return "No Coffee"

            else:
                return "No Coffee"
        else:
            return None
    else:
        return None

# TODO: 5 Process the coins(identify how many of each coin has been put in.
def pay(coin1, coin2, coin3, coin4 ):
    print("Please insert coins")
    quarter_paid = input("How many quarters?: ")
    dime_paid = input("How many dimes?: ")
    nickel_paid = input("How many nickels?: ")
    penny_paid = input("How many pennies?: ")

    total_quarter = float(quarter_paid) * coin1
    total_dime = float(dime_paid) * coin2
    total_nickel = float(nickel_paid) * coin3
    total_penny = float(penny_paid) * coin4
    paid = total_quarter + total_dime + total_nickel + total_penny
    return paid


# TODO: 6 Check transaction is successful (compare the total no of coins put in to price
def check_transaction(order2, paid, cash):
    price = order2["cost"]
    change = 0
    refund = 0
    if paid > price:
        change += round(paid - price , 2)
        cash += price
        return "change", change, cash
    elif paid < price:
        refund += paid
        cash += price
        return "refund" , refund, cash
    else:
        cash += price
        return "no change" , change, cash



# TODO: 10 Put everything together

def coffee_machine():
    global machine_money, coffee_amount, milk_level, water_level
    user_command = True
    while user_command:
        brewing_coffee = True
        make_choice = input("What would you like? Espresso / Latte / Cappuccino: ").lower()
        report_or_off = report_off(make_choice)
        if report_or_off == "False":
            user_command = False
            print("\n" * 50)
            coffee_machine()
        elif report_or_off == "True":
            user_command = False
            print(report(water_level, milk_level, coffee_amount, machine_money))
            coffee_machine()

        while brewing_coffee:
            ordered = user_order(make_choice, menu)

            resource_amount = check_resources(ordered, water_level, milk_level, coffee_amount)
            print(resource_amount)
            if resource_amount == "Coffee":
                order = user_order(make_choice, menu)
                print(f"Your {make_choice} costs: {order["cost"]}")
                paid_amount = pay(quarter, dime, nickel, penny)
                print(paid_amount)
                transaction_statement, user_money, machine_money  = check_transaction(ordered, paid_amount, machine_money)

                if transaction_statement == "change":
                    print(f"Here is ${user_money} in change")
                    water_level, milk_level, coffee_amount, outcome = make_coffee(ordered, make_choice, water_level, milk_level,
                                                                                  coffee_amount)
                    print(outcome)
                elif transaction_statement == "no change":
                    print(f"No change needed")
                    water_level, milk_level, coffee_amount, outcome = make_coffee(ordered, make_choice, water_level, milk_level,
                                                                                  coffee_amount)
                    print(outcome)
                else:
                    print(f"Sorry that's not enough money. Money refunded: {user_money}")
                    brewing_coffee = False

            elif resource_amount == "No coffee":
                brewing_coffee = False
                print(resource_amount)
                print("Sorry not enough resources")
            else:
                brewing_coffee = False

coffee_machine()
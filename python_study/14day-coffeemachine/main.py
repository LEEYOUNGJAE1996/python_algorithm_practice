# 230305

import coffee

resource = coffee.resources
menu = coffee.MENU


def enough_resource(choice, resource):
    if menu[choice]["ingredients"]["water"] > resource["water"]:
        return False, "water"
    if menu[choice]["ingredients"]["milk"] > resource["milk"]:
        return False, "milk"
    if menu[choice]["ingredients"]["coffee"] > resource["coffee"]:
        return False, "coffee"
    else:
        return True, "nothing"


def enter_money():
    print("how many coin?")
    quarters = int(input("Quaters >> ")) * 0.25
    dimes = int(input("Dimes >> ")) * 0.1
    nickles = int(input("Nickles >> ")) * 0.05
    pennies = int(input("Pennies >> ")) * 0.01
    return quarters + dimes + nickles + pennies


def enough_money(money, choice):
    if money < menu[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return True


def cal_resource(choice, resource):
    resource["water"] -= menu[choice]["ingredients"]["water"]
    resource["milk"] -= menu[choice]["ingredients"]["milk"]
    resource["coffee"] -= menu[choice]["ingredients"]["coffee"]
    return resource


def cal_money(choice, money):
    money -= menu[choice]["cost"]
    global machine_money
    machine_money += menu[choice]["cost"]
    return money,


machine_money = 0
turn_on = True
while turn_on:
    choice = input(
        "What would you like ? (espresso/latte/cappuccino): ").lower()
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        # 자원과 비교하는 함수
        canBuy, shortage_resource = enough_resource(choice, resource)
        if canBuy:
            money = round(enter_money(), 2)
            can_buy_coffee = enough_money(money, choice)
            if can_buy_coffee:
                # TODO : 함수로 있는 자원을 없애고 남은 계산 후 남은 금액 돌려주는
                print(f"Here is your {choice}. Enjoy!")
                resource = cal_resource(choice, resource)
                refund = cal_money(choice, money)
                if refund != 0:
                    print(f"Here is ${refund} in change.")
        else:
            print(f"Sorry there is not enough {shortage_resource}")
    elif choice == "report":
        print(f"Water : {resource['water']}ml")
        print(f"Milk : {resource['milk']}ml")
        print(f"Coffee : {resource['coffee']}g")
        print(f"Money : ${machine_money}")
    elif choice == "off":
        turn_on = False
    else:
        print("you have entered an invalid value.")


# 개선해야 할점
# 함수를 작성한 후 함수에 대한 설명을 추가할 것
# DOCSTRING("""    """ )을 통해서 설명을 추가해야한다.

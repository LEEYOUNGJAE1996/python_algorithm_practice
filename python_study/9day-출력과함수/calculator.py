import cal_art


def cal(a, b, operation):
    """
    operation에 따라서 원하는 계산 결과를 반환한다.
    +의 경우 a+b
    -의 경dn a-b
    *의 경우 a*b
    /의 경우 a/b
    의 결과를 반환    
    """
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a/b
    else:
        return False

# 새로운 수를 ? 아님 기존의 수를?


def continueOrNot(input):
    if input.lower() == 'y':
        return False, True
    elif input.lower() == 'n':
        return True, True
    else:
        print("you enter worng value.system is out")
        return False, False


print(cal_art.logo)

# start
newthing = True
result = 0
should_continue = True
while should_continue:
    if newthing == True:
        result = 0
        fir_number = float(input("What's the first number >> "))
    print("+")
    print("-")
    print("*")
    print("/")
    op = input("Pick on operation >> ")
    sec_number = float(input("What's the next number >> "))
    result = cal(a=fir_number, b=sec_number, operation=op)
    if result == False:
        print("you enter worng value")
    else:
        print(f"{fir_number} {op} {sec_number} = {result}")
    newthing, should_continue = continueOrNot(input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation >>"))


# 강의 방식 재귀함수를 활용
#############################################################################
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(cal_art.logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
###############################################################################################

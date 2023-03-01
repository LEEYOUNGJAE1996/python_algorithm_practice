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
        return False
    elif input.lower() == 'n':
        return True
    else:
        print("you enter worng value. try again")
        return False


print(cal_art.logo)

# start
newthing = True
result = 0
while True:
    if newthing == True:
        result = 0
        fir_number = int(input("What's the first number >> "))
    print("+")
    print("-")
    print("*")
    print("/")
    op = input("Pick on operation >> ")
    sec_number = int(input("What's the next number >> "))
    result = cal(a=fir_number, b=sec_number, operation=op)
    if result == False:
        print("you enter worng value")
    else:
        print(f"{fir_number} {op} {sec_number} = {result}")
    newthing = continueOrNot(input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation >>"))

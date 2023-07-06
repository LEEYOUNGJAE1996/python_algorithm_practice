# 230707
# 현재 상황에서 가장 좋은 것만 고르는 방법

# 500, 100, 50, 10 동전 무한히 존재 N 것를러 줘야할 최소



# pay = int(input("손님이 내야할 금약 : "))
# money = int(input("손님이 낸 금액 : "))
# returnMoney = 0
# if money < pay :
#     print("지불 불가")
# else :
#     returnMoney =  money-pay
#     N = returnMoney // 500
#     returnMoney = returnMoney % 500
#     N += returnMoney // 100
#     returnMoney = returnMoney % 100
#     N += returnMoney // 50
#     returnMoney = returnMoney % 50
#     N += returnMoney // 10
#     print(N)

# 답안
n = int(input())
count = 0
moneyList = [500,100,50,10]
for money in moneyList:
    count += n // money
    n %= money
print(count)
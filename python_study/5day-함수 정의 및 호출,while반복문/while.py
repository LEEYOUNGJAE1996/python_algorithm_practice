# while 반복문을 구현한다.
# 230221
# for구문의 경우
# 1) for item in list_of_item:
#       #do someting to each item
# 2) for number in range(a,b):
#       print(number)  ---- between a and b

# while 구문의 경우
# while something_true:
#   #Do something repeatedly
# 보통 while 구문의 경우 특정 부분에 대해서
# 설정한 부분에 도달할 때까지 수없이 많은 반복이 필요로 하는 경우
# 사용하는 경우가 많다.
result = True
i = 0
while result:
    i += 1
    print(i)
    if i == 100:
        result = False

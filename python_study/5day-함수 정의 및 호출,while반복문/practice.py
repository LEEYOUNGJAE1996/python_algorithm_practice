# 함수 정의 및 호출 사용하기
# 230221

def my_fuction():
    print("hello")
    print("Bye")


def swipe(data, data2):
    data, data2 = data2, data
    return data, data2


my_fuction()

data = 1
data2 = 2

print(swipe(data, data2))
# 230322

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8,9,10,11,12,13))

def calculate(**kwargs):
    # print(type(kwargs))
    # print(kwargs) 
    # key 와 value를 나눠서 for구문 다루기 item()
    for key, value in kwargs.items():
        print(key, value)
calculate(add=3 , multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        # 디폴트 설정?
        if self.make == None:
            self.make = 'ki'
        self.model  = kw.get('model')
        if self.model == None:
            self.model = '000'
#전부 입력하지 않을 경우 crash 
# 그렇다면 어떻게 문제를 해결할 것인가?
car = Car(make = 'h')
print(car.model)
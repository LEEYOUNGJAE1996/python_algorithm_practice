# 230312

# 상위 클래스

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale.")

# 상속받는 클래스-> 자식클래스


class Cat(Animal):
    def __init__(self):
        # 상위 클래스의 attributes 와 methods를 상속받기 위한 코드
        # 필수는 아니다. 왜???
        super().__init__()
    # 상속받은 메소드에 새로운 값 입력하기

    def breathe(self):
        # 상위 클래스의 같은 이름의 메소드 기능을 상속
        super().breathe()
        print("so cute!")
    # Cat의 독자적인 method

    def attack(self):
        print("punch")


soda = Cat()

soda.breathe()
soda.attack()

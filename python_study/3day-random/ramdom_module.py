import random
# start 부터 end 사이의 정수를 출력한다. - 각 부분을 포함한다.
random_integer = random.randint(1, 10)
print(random_integer)

# 소수점 자리를 0 <=  x < 1 범위를 램덤으로 생성
random_float = random.random()
print(random_float)

# random 연습
random_side = random.randint(0, 1)

if random_side == 1:
    print("Heads")
else:
    print("Tails")

state1 = ["인천"]
state2 = ["서울"]
state3 = ["광주"]

state_of_korea = ["인천", "서울", "광주"]
print(state_of_korea[1])
print(state_of_korea[-2])
# print(state_of_korea[시작:끝+1:간격])
print(state_of_korea[0:3:2])
state_of_korea.append("제주도")
print(state_of_korea)

#

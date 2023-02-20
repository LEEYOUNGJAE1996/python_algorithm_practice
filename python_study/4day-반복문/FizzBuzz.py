# #fizzbuzz 면접 문제

# 기본적인 룰
# 많은 아이들이 동그랗게 둘러앉아 시계 방향으로 움직인다.
# 처음시작 하는 아이는 '1'을 말하며 옆으로 순서를 넘기며 숫자는 1씩 증가한다.
# 그 중
# 3으로 나누어지는 경우 Fizz를 말하고
# 5로 나누어지는 경우 Buzz라 답한다.
# 마지막으로 3,5로 나누어지는 경우 FizzBuzz라고 말하는 게임이다.


# 조건 1.1 ~ 100까지 숫자 반복
# 조건 2. 3으로 나눠지는 5로 나눠지는 15로 나눠지는 수 구분하기
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        num = "FizzBuzz"
    elif num % 3 == 0:
        num = "Fizz"
    elif num % 5 == 0:
        num = "Buzz"
    else:
        num = str(num)
    print("Player: " + num)

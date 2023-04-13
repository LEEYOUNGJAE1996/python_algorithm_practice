# 230309
# 제너레이터와 uield를 사용
# 일반적인 방식으로 해당 진행 과정을 보여주기 위한 방식
def fib_generator():
    a, b = 0, 1
    while True:
        # yield를 통해 제너레이터에 b의 값을 저장
        yield b
        a, b = b, a+b


if __name__ == "__main__":
    # fg에 fib_generator 할당
    fg = fib_generator()
    #  next 함수를 통해 fg에 저장된 값을 하나씩 불러 온다.
    # generator 와 yield 에 대해서
    # https://dojang.io/mod/page/view.php?id=2412
    for _ in range(13):
        print(next(fg), end=" ")

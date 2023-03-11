# 230308
import math

# 일반적인 형태 현재의 값은 그전과 -2위치의 값을 더한 값이다.
# 시간복잡도(O(n))


def find_fibonacci_iter(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

# 재귀함수를 이용
# 시간복잡도(O(2**n))


def find_fibonacci_rec(n):
    if n < 2:
        return n
    return find_fibonacci_rec(n-1)+find_fibonacci_rec(n-2)

# 일반식을 통한
# 시간복잡도(O(1))


def find_fibonacci_form(n):
    # 5 root
    sq5 = math.sqrt(5)
    phi = (1 + sq5)/2
    # 내림! floor
    return int(math.floor(phi ** n/sq5))


def test_find_fib():
    n = 10
    assert (find_fibonacci_form(n) == 55)
    assert (find_fibonacci_iter(n) == 55)
    assert (find_fibonacci_rec(n) == 55)
    print("passed test")


if __name__ == "__main__":
    test_find_fib()

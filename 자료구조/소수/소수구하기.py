# 230309

import math
import random


# n까지 수를 직접 나눠보는 방식
def finding_prime(number):
    num = abs(number)
    if num < 4:
        return True
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

# 제곱근을 이용

# m = n**(1/2) 라고 가정하에 푼다.
# 만약 위의 가정이 같다면 n = a* b 일 경우 m * m = a*b 이다.
# m은 실수 n,a,b는 자연수이다.

# 1. a>n 이면 b < m
# 2. a = m 이면 b = m
# 3. a < m 이면 b > m 이다.

# 세 가지의 경우 전부 min(a,b) <= m이므로, m까지의 수 중 n과 나누어 떨어지는 수를 발견할 것이다.
# 그 결과로 n은 소수가 아님을 증명할 수 있게 된다.


def finding_prime_sqrt(number):
    num = abs(number)
    if num < 4:
        return True
    for x in range(2, int(math.sqrt(num))+1):
        if num % x == 0:
            return False
    return True


# 페르마의 소정리
# p가 소수이고 a가 p의 배수가 아니면 , a**(p-1) == 1(mod p)
# p가 소수라면 , 모든 정수 a에 대해 a**p == a(mod p) (위의 식에서 a를 곱한 것)
# mod의 의미?? -->한 마디로 임의의 소수 p와 서로소인 한 수의 (p−1)승을 p로 나눈 나머지는 무조건 1이라는 정리.

def finding_prime_fermat(number):
    if number <= 102:
        for a in range(2, number):
            if pow(a, number-1, number) != 1:
                return False
        return True
    else:
        for i in range(100):
            a = random.randint(2, number-1)
            if pow(a, number-1, number) != 1:
                return False
        return True


def Test():
    number1 = 17
    number2 = 20
    assert (finding_prime(number1) is True)
    assert (finding_prime(number2) is False)
    assert (finding_prime_sqrt(number1) is True)
    assert (finding_prime_sqrt(number2) is False)
    assert (finding_prime_fermat(number1) is True)
    assert (finding_prime_fermat(number2) is False)
    print("passed test")


Test()

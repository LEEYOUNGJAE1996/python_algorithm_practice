# 분수를 다루기 위한 모듈
from fractions import Fraction


def rounding_floats(num1, place):
    # 특정 위치에서 반올림
    return round(num1, place)


def float_to_fractions(num):
    return Fraction(*num.as_integer_ratio())


def get_denominator(num1, num2):
    """분모를 반환한다."""
    a = Fraction(num1, num2)
    return a.denominator
    # denominator == 분모


def get_numerator(num1, num2):
    """분자를 반환"""
    a = Fraction(num1, num2)
    return a.numerator


def test_testing_float():
    num1 = 1.25
    num2 = 1
    num3 = -1
    num4 = 5/4
    num5 = 6
    # assert 조건식 , 에러 메세지 출력
    assert (rounding_floats(num1, num2) == 1.2)
    assert (rounding_floats(num1 * 10, num3) == 10)
    assert (float_to_fractions(num1) == num4)
    assert (get_denominator(num2, num5) == num5)
    assert (get_numerator(num2, num5) == num2)
    print("테스트 통과")


# 처음 main 문장 시작하는 파일이면 동작
if __name__ == "__main__":
    test_testing_float()

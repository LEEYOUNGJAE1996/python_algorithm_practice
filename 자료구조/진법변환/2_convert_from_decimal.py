# 230307

# 십진수를 n진법으로
def convert_from_decimal(num, base):
    #  제곱근과 결과값
    multiplier, result = 1, 0
    while num > 0:
        result += num % base * multiplier
        multiplier *= 10
        num = num // base
    return result


def test():
    num, base = 9, 2
    assert (convert_from_decimal(num, base))
    print("pass the test!")


if __name__ == "__main__":
    test()

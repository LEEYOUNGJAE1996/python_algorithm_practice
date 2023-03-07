# 230307

# 2 이상 20미만의 범위안의 진수로 10진수를 변환하는 함수
def convert_from_decimal(num, base):
    # 10 이상의 값을 표현하기 위해  String으로 값을 저장 후 위치로 해당 값을 가져온다.
    # 결과 리턴의 결과도 int형이 아닌  String 형태를 가진다.
    strings = "0123456789ABCDEFGHIJ"
    result = ""
    while num > 0:
        # 나머지를 통해 해당 위치의 값을 불러올 인덱스를 저장
        digit = num % base
        #  주의할 점  result를 뒤에서 더해야한다. 안그럼 역으로 저장
        # += 연산자를 쓰면 잘못된 값을 반환
        result = strings[digit] + result
        num = num // base
    return result


def test():
    num, base = 31, 16
    assert (convert_from_decimal(num, base) == "1F")
    print("passed test!")


if __name__ == "__main__":
    test()

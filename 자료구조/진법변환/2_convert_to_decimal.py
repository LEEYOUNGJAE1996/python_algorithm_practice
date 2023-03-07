# 230307

# 이진법을 십진법으로 바꾸기 위한 함수
# 이 때 굳이 이진수가 아니여도 괜찮다. base가 2~9 범위 내의 수라면 변환이 가능하다.
def convert_to_decimal(num, base):
    # 2의 0제곱부터
    multiplier, result = 1, 0
    while num > 0:
        # n진법으로 표현된 값을 각 1의자리부터 하나씩 값을 가져오는 방식
        result += num % 10 * multiplier
        multiplier *= base
        num = num // 10
    return result


def test_convert_to_decimal():
    num, base = 1001, 2
    assert (convert_to_decimal(num, base) == 9)
    print("테스트 통과!")


# 지금 실행하는 파일이 시작점인지
if __name__ == "__main__":
    test_convert_to_decimal()

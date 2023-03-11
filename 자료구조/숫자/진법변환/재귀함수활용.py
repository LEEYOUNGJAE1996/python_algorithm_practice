# 230307

def convert_dec_to_any_base(num, base):
    # 2 ~ 16 진수까지 커버
    convertString = "012456789ABCDEF"
    # 재귀함수의 방식을 이해할 필요가 있다.
    # 끝으로 넘어가 끝에서 점점 다가온다.
    if num < base:
        return convertString[num]
    else:
        return convert_dec_to_any_base(num//base, base) + convertString[num % base]


def test():
    num, base = 9, 2
    assert (convert_dec_to_any_base(num, base) == "1001")
    print("passed test")


if __name__ == "__main__":
    test()

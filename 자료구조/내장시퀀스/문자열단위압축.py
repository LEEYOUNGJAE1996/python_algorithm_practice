# 230320

def str_compression(s):
    count, last = 1, ""
    list_aux = []
    # enumerate : 인덱스와 동시에 리스트 형태의 값을 같이 인자에 만들어준다.
    # 아래와 같은 경우 i 에는 인덱스 값이 c의 경우에는 s의 i번째 인덱스에 있는 값이 대입된다.
    for i, c in enumerate(s):
        if last == c:
            # 시작 알파벳과 다음 문자가 같은 경우 count가 증가한다.
            count += 1
        else:
            # 시작 알파벳과 다르며 시작점이 아닌 경우 지금까지 증가한 count를 시작한 알파벳의 다음으로 입력함으로써
            # 현재 시작점인 알파벳이 몇개가 들어있는지 표시한다.
            # 이때 문제점은 연속된 값만 판단이 가능하다는 것이다.
            # 뒤에 다른 값이 나온 후 이후에 처음과 같은 값이 나온 경우 별개의 경우로 판단한다.
            if i != 0:
                list_aux.append(str(count))
            # list_aux에는 처음 시작하는 알파벳의 시작이 들어간다.
            list_aux.append(c)
            count = 1
            last = c
    list_aux.append(str(count))
    return "".join(list_aux)


if __name__ == "__main__":
    result = str_compression('aaabbbbbaabbwwweffes')
    print(result)

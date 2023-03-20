# 230320

def reverser(string1, p1=0, p2=None):
    if len(string1) < 2:
        return string1
    p2 = p2 or len(string1)-1
    # 모든 문자열의 알파벳의 순서를 변경한다.
    while p1 < p2:
        string1[p1], string1[p2] = string1[p2], string1[p1]
        p1 += 1
        p2 -= 1


def reversing_words(string1):
    reverser(string1)
    print(string1)
    p = 0
    start = 0
    while p < len(string1):
        if string1[p] == " ":
            # 공백을 기준으로 단어를 나눠 다시 반전
            reverser(string1, start, p-1)
            print(string1)
            start = p+1
        p += 1
    # 마지막 단어를 반전
    # 마지막 단어는 다음에 공백이 없으므로 따로 진행
    reverser(string1, start, p-1)
    # 리스트형을 다시 합쳐 주기 위해서는 다음과 같은  join메서드를 사용
    return "".join(string1)


string1 = "1.오늘 저녁은 무엇을 먹을까?"
# 문자열의 경우 불변형 타입이기에 리스트 형태로 바꾼 후 진행할 필요가 있다.
string2 = reversing_words(list(string1))
print(string2)


# 반복문 한 번만 사용하는 방법

def reverse_words_brute(string):
    word, sentence = [], []
    for character in string:
        if character != " ":
            word.append(character)
        else:
            if word:
                sentence.append("".join(word))
                word = []
    # 마지막 단어 추가
    if word != "":
        sentence.append("".join(word))
    sentence.reverse()
    # 띄어씌기를 한 문자열에 join을 수행해야 문자열을 합치는 중간에 띄어쓰기가 포함되서 문자열을 만든다.
    return " ".join(sentence)


string = "2.오늘 저녁은 무엇을 먹을까?"
# 문자열의 경우 불변형 타입이기에 리스트 형태로 바꾼 후 진행할 필요가 있다.
string2 = reverse_words_brute(list(string))
print(string2)

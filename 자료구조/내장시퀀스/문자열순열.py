# 230320
# 문자열 순열
# 순열의 의미 - 순열은 서로 다른 n개 중 r개를 골라 순서를 고려해 나열한 경우의 수이다
# 입력으로 들어오는 길이 n의 문자열에서 n 개 문자를 모두 선택하는 경우의 문자열을 나열

import itertools

# 시간 복잡도 n!


def perm(s):
    print(s)
    if len(s) < 2:
        return s
    res = []
    for i, c in enumerate(s):
        for count in perm(s[:i] + s[i+1:]):
            res.append(c + count)
            print(res)
    return res


def perm2(s):
    res = itertools.permutations(s)
    return ["".join(i) for i in res]


if __name__ == "__main__":
    value = "012"
    print("perm()의 결과 : ", perm(value))
    print("perm2()의 결과 : ", perm2(value))

# 230320

def is_palindrome(s):
    l = s.split(" ")
    s2 = "".join(l)
    return s2 == s2[::-1]


def is_palindrome2(s):
    l = len(s)
    f, b = 0, l-1
    while f < l//2:
        while s[f] == " ":
            f += 1
        while s[b] == " ":
            b -= 1
        if s[f] != s[b]:
            return False
        f += 1
        b -= 1
    return True


def is_palindrome3(s):
    s = s.strip()
    if len(s) < 2:
        return True
    if s[0] == s[-1]:
        return is_palindrome3(s[1:-1])
    else:
        return False


if __name__ == '__main__':
    string1 = '토마토'
    string2 = '다시 합창합시다'
    string3 = '아 오늘은 여기까지입니다'
    print('stirng1의 1번째 방법으로 확인 : ', is_palindrome(string1))
    print('stirng1의 2번째 방법으로 확인 : ', is_palindrome2(string1))
    print('stirng1의 3번째 방법으로 확인 : ', is_palindrome3(string1))
    print('stirng2의 1번째 방법으로 확인 : ', is_palindrome(string2))
    print('stirng2의 2번째 방법으로 확인 : ', is_palindrome2(string2))
    print('stirng2의 3번째 방법으로 확인 : ', is_palindrome3(string2))
    print('stirng3의 1번째 방법으로 확인 : ', is_palindrome(string3))
    print('stirng3의 2번째 방법으로 확인 : ', is_palindrome2(string3))
    print('stirng3의 3번째 방법으로 확인 : ', is_palindrome3(string3))

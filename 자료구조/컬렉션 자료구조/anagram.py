# 230326

from collections import Counter
# 해당 문장의 글자 수를 측정한다. 
# 포함된 알파벳과 수가 같은 경우 anagram 이라고 한다.

def anagram(s1,s2):
    counter = Counter()
    for letter in s1:
        counter[letter] +=1
    for letter in s2:
        counter[letter] +=1
    print(counter)
    for i in counter.values():
        if i == 1:
            return False
    return True

def test():
    s1 = 'marina'
    s2 = 'aniram'
    assert(anagram(s1,s2) is True)
    s1 = 'google'
    s1 = 'gouglo'
    assert(anagram(s1,s2) is False)
    print('success')

if __name__ == '__main__':
    test()
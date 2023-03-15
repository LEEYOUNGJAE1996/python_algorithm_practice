# 230315

# append
a = []
a.append('과자')
print(a)

# extend()
b = []
b.extend("extend")
print(b)
# 아래와 같다.
b = []
for letter in "extend":
    b.append(letter)
    print(b)


# insert
# insert(위치, 넣을 값)
c = ['과자', '먹을까?']
print(c)
c.insert(0, '무슨')
print(c)

# remove()

c.remove('먹을까?')
print(c)

# pop()
print(c.pop(1))
print(c)

# del 문
d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(d)
del d[3:5]
print(d)

# index()
print(d.index(8))
# print(d.index(4))  예외 발생

e = [1, 1, 2, 3, 4, 5, 7, 5, 6, 5, 3, 2]
print(e.count(5))
print(e.count(1))
print(e.count(9))

# sort
f = [1, 3, 2, 9, 5, 10, 4, 6, 9, 10]
print(f)
f.sort()
print(f)
f.sort(reverse=True)
print(f)

# reverse()
f = [1, 3, 2, 9, 5, 10, 4, 6, 9, 10]
print(f)
f.reverse()
print(f)

# 리스트 언패킹
g, *h = [1, 2, 3, 4, 5, 6, 7]
print(g)
print(h)

*g, h = [1, 2, 3, 4, 5, 6, 7]
print(g)
print(h)


# 리스트 컴프리헨션

a = [y for y in range(1900, 1940) if y % 4 == 0]
print('a : ', a)
b = [2**i for i in range(13)]
print('b : ', b)
c = [x for x in a if x % 2 == 0]
print('c : ', c)
d = [str(round(355/113.0, i) for i in range(1, 6))]
print('d : ', d)
# split 하는 경우 리스트 형태로 반환
words = "Buffy is awesome and a vampire slayer'".split()
# 리스트 형태로 나눠진 단어들을 각각 적용하는
e = [[w.upper(), w.lower(), len(w)] for w in words]
print('e : ', e)

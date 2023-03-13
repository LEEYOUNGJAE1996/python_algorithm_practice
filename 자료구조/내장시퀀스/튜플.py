# 230313

# 튜플

import collections
t1 = 1234, '안녕'
print(t1)

# 중첩이 가능하다.
t2 = t1, (1, 2, 3, 4, 2, 4, 5, 6, 2, 1)
print(t2)

# count
t3 = (1, 2, 3, 4, 2, 4, 5, 6, 2, 1)
print(t3.count(2))


# index
t4 = (1, 2, 3, 4, 2, 4, 5, 6, 2, 1)
print(t4.index(3))

# unpacking
x, *y = (1, 2, 3, 4)
print('x ', x, ' y ', y)
*x, y = (1, 2, 3, 4)
print('x ', x, ' y ', y)


# namedtuple
Person = collections.namedtuple('Person', 'name age gender')
p = Person("이영재", 28, '남')
print(p[0])
print(p.name)

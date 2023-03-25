# 230325

# # set method
# # set은 중괄호로 생성한다.

# set_container = {'공부하자','파이썬'}

# print(set_container)
# # add(value)
# set_container.add('데이터 분석가가 되자')
# print(set_container)

# # update |=
# set_container.update({'Devops 개발자도?'})
# print(set_container)
# set_container |= {'Clouding에 대해서 공부를'}
# print(set_container)

#union() , | 연산자
# 기본적으로 update와 유사하지만 데이터를 적용한 변수에 적용하는 것이 아닌
# 메서드와 연산자를 적용한 결과를 반환하고 새로운 set 데이터 타입을 통해 저장한다.

set_container = {'공부하자','파이썬'}
new_set=set_container.union({'기술 발전이 너무 빠르다.'})
print(set_container)
print(new_set)
new_set=set_container | {'Clouding에 언제하지'}
print(set_container)
print(new_set)
print(type(set_container))

# # intersection , &
# # 교집합의 복사본을 반환
# print(set_container.intersection(new_set))
# print(set_container&new_set)

# # difference , - 연산자
# # 차집합의 복사본을 반환
# print(new_set.difference(set_container))
# print(new_set - set_container)

# # clear()
# print(new_set.clear())

#discard(), remove() , pop()
set_container.discard('공부하자')
print(set_container)
print(set_container.pop())
print(set_container)


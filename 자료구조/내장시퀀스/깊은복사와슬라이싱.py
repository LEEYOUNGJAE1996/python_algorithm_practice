# 230311

import copy
myList = [1, 2, 3, 4, 5]
newList = myList[:]
newList2 = list(myList)


print(myList)
print(newList)
print(newList2)

# set의 깊은 복사

people = {"가", "나", "다"}
who = people.copy()
who.discard("가")
who.remove("나")
print(who)
print(people)


# dictionary의 깊은 복사

people_dic = {"가", "나", "다"}
who_dic = people_dic.copy()
print(who_dic)

# 기타 객체의 깊은 복사할 때는  copy모듈을 사용
myObj = "다른 어떤 객체"
newObj = copy.copy(myObj)  # 얕은 복사
newObj2 = copy.deepcopy(myObj)  # 깊은복사
# 위의 차이점은 무엇일까?
print(newObj)
print(newObj2)

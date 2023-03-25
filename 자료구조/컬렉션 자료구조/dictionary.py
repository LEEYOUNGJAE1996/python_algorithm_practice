# 230325

# dictionary 

dict1 = {}
print(type(dict1))
# 값을 추가하는 방법 1
dict1['name'] = 'young'
dict1['job'] = 'None'
print(dict1)

#dict 초기화하며 생성1
dict2 = {'name':'young' , 'job': 'None'}
print(dict2)
#dict 초기화하며 생성2
dict3 = dict(name='young',job = 'None')
print(dict3)
#dict 초기화하며 생성3
dict4 = dict([('name','young'),('job','None')])
print(dict4)

# setdefault()
dict5 = {}
print(dict1.setdefault('name','young'))
print(dict5)
print(dict5.setdefault('name','young'))

#update()
print(dict1)
dict1.update({'name':'영재'})
print(dict1)


from collections import Counter

# 해당 리스트에 항목에 발생 확수를 매핑하는 딕셔너리를 생성한다.
list_ex = [1,2,3,5,1,2,3,4,5,1,2,3,4,5,1,2,4,5]
# counter 객체 생성
dict_ex = Counter(list_ex)
print(dict_ex)
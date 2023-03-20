# 230321

# comprehension 미적용
number = [1, 2, 3]
new1 = []
for item in number:
    num = item + 1
    new1.append(num)
print('new1 : ', new1)
# comprehension 적용
new2 = [item + 1 for item in number]
print('new2 : ', new2)

# ex) range 활용 예시
new3 = [num * 2 for num in range(1, 5)]
print('range_new3 : ', new3)

# 제곱수 예제

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 문제 제곱한 값을 저장하는 새로운 리스트를 만들어라
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

# 짝수 필터링
result = [num for num in numbers if num % 2 == 0]
print(result)

# 겹치는 데이터 체크
# file1, file2 데이터를 가져오는 방법은?

with open('./python_study/25day-List,Dictionary에대한이해/file1.txt') as file1:
    file1_data = file1.readlines()

with open('./python_study/25day-List,Dictionary에대한이해/file2.txt') as file2:
    file2_data = file2.readlines()

# in keyword의 경우 해당 리스트 안에 비교하는 값이 있는지 파악한다.
# 있는 경우 True
result = [num for num in file1_data if num in file2_data]
print(result)

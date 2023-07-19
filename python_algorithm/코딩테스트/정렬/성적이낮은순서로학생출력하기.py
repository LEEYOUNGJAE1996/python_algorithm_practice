# 230719

# 성적이 낮은 순서로 학생 출력하기

# n명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다. 각 학생의 이름과 성정 정보가 
# 주어졌을 때 성적이 낮은 순서대로 이름을 출력하는 프로그램을 작성하시오.

# 입력조건
# 1. 첫 번째 줄에 학생의 수 N 이 입력된다.
# 2. 두 번째 줄부터 N +1 번째 줄에는 학새으이 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가
# 공백으로 구분되어 입력된다. 문자열 A의 길이와 학생의 성적은 100 이하의 자연수이다.


# 출력 조건
# 모든 학생의 이름을 성적이 낮은 순서대로 출력한다. 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.


# TODO : n의 입력을 받는다.
n = int(input())

# TODO : n의 학생 수의 이름과 점수를 받는다.
array = []
for i in range(n):
    name, grade = input().split()
    array.append({"Name":name,"Grade" :int(grade)})
#매우 중요 하나의 set 또는 dictionary 에서 key 값이 존재하는 경우 아래와 같이 sorted에서 lambda를 적용하여 해결이 가능하다.
sortedArray = sorted(array, key= lambda x : x['Grade'])

# 정렬이 수행된 결과를 출력
for student in sortedArray:
    print(student['Name'],end= " ")
# 230719

#  계수 정렬 구현

array = [2,5,5,7,7,5,7,5,2,21,4,54,6,7,8,9,67,5]

count = [0] * (max(array) +1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
for i in range(len(count)):
    for j in range(count[i]):
        print(i,end="")
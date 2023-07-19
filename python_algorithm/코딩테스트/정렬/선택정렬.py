# 230718

# 선택 정렬 기본


array = [2,6,47,4,64,7,3456,35,3]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# 시간 복잡도 O(N^2)
import random
import time

# 임의의 데이터를 이미 정렬된 부분의 적절한 위치에 삽인해 가며 정렬하는 방식이다.


def insertionSort(array, N):
    for i in range(2, N):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
        print(array)
    return array


def checkSort(arr, n):
    isSorted = True
    for i in range(1, n):
        if (arr[i] > arr[i+1]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted:
        print("정렬완료")
    else:
        print("정렬 오류")


N = 10
arr = []
arr.append(None)
for i in range(N):
    arr.append(random.randint(1, N))
start_time = time.time()
insertionSort(arr, N)
end_time = time.time() - start_time
print("선택 정렬의 실행 시간 ( N = %d) : %0.3f" % (N, end_time))
checkSort(arr, N)

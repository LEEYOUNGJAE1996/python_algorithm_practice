import random
import time


# def quickSort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left, equal, right = [], [], []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num > pivot:
#             right.append(num)
#         else:
#             equal.append(num)
#         print(quickSort(left) + equal + quickSort(right))
#     return quickSort(left) + equal + quickSort(right)
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)


def checkSort(arr, n):
    isSorted = True
    for i in range(0, len(arr)):
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
# arr.append(None)
for i in range(N):
    arr.append(random.randint(1, N))
start_time = time.time()
print(quickSort(arr))
end_time = time.time() - start_time
print("Quick 정렬의 실행 시간 ( N = %d) : %0.3f" % (N, end_time))
# checkSort(arr, N)

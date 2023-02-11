# 이진 탐색 알고리즘 함수
# 이진 탐색 알고리즘 선행조건 - 정렬되어있는 배열에서 적용
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if item < arr[mid]:
            high = mid - 1
        elif arr[mid] > item:
            low = mid + 1
        else:
            return mid
    return -1


# 실행문
arr = [2, 4, 5, 9, 35, 58, 99]
item = 9
result = binary_search(arr, item)
if result == -1:
    print(item, "을 찾을 수 없습니다.")
else:
    print(item, "은 ", result, "번 째에 존재합니다.")

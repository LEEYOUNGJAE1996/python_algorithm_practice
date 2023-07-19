# 230719

# 퀵 정렬 구현

array = [2,767,3,4,487769,5,4453,7,25,423,35,1,7645,345]

def quick(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 첫 번째 원소를 사용한다.
    left = start + 1
    right = end
    while left <= right:
        #  피벗보다 큰 데이터를 찾을 때까지 반복? 왼쪽부터 시작하여 피벗보다 큰 수를 찾는 다는 의미 그 위치를 기억한다.
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복? 오른쪽부터 시작하여 오른쪽보다 작은 수를 찾는 다는 의미 그 위치를 기억한다.
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right : # left의 위치와 right의 위치가 바뀌었다면 right의 위치와 pivot 위치값을 변경함으로써 기준을 변경
            array[right], array[pivot] = array[pivot], array[right]
        else : #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left],array[right] = array[right] , array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행 재귀함수를 통해 반복
    print(start, right, end)
    quick(array,start, right -1)
    quick(array,right +1, end)
quick(array,0, len(array)-1)
print(array)


# 파이썬의 장점을 살린 퀵 정렬 소스 코드
array = [2,767,3,4,487769,5,4453,7,25,423,35,1,7645,345]

def quickPython(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    leftSide = [x for x in tail if x <= pivot]
    rightSide = [y for y in tail if y > pivot]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 , 전체 리스트를 반환
    return quickPython(leftSide) + [pivot] + quickPython(rightSide)

print(quickPython(array))

# 퀵 정렬의 시간 복잡도 O(NlogN)
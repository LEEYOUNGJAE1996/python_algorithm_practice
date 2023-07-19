# 230719

# 위에서 아래롤 하나의 수열에는 다양한 수가 존재한다 .이러한 수는 크기에 상관없이 나열되어 있다. 
# 이 수를 큰수부터 작은 수의 순서로 정렬해야 한다. 수열을 내림차순으로 정렬하는 프로그램을 만드시오


# 입력 조건 
# 1. 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다.
# 2. 둘째 줄부터 N +1 번째 줄ㄲ자ㅣ N개의 수가 입력된다. 수의 범위는 1이상 100000이하의 자연수 이다.

# 출력 조건
# 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다. 동일한 수의 순서는 자유롭게 출력해도 괜찮다.

n = int(input())
array = [int(input()) for x in range(n)]

# 순서 정렬 하는 것 그냥 파이썬 으로 해도 되지만 우선 퀵도 구현해보자

array1 = array
array1 = sorted(array,reverse=True)
print(array1)

def quick(array, start, end):
    if start >= end:
        return 
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end  and array[left] >= array[pivot]:
            left += 1
        while right > start and array[right] < array[pivot]:
            right -=1
        if left > right :
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right], =array[right], array[left]

        quick(array,start,right -1)
        quick(array,right + 1, end)

def quickPython(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    leftSide = [x for x in tail if x >= pivot]
    rightSide = [x for x in tail if x < pivot]
    return quickPython(leftSide) + [pivot] + quickPython(rightSide)

print(quickPython(array))
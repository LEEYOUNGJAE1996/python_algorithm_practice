# 230720

# 이진 탐색을 구현하는 2가지 방법

# by 재귀

def binary_re(array,target, start,end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target :
        return mid
    elif array[mid] < target:
        binary_re(array,target,mid+1,end)
    else :
        binary_re(array,target,start,mid-1)


# by for
def binary_for(array,target,start,end):
    while start < end:
        mid = (start + end) // 2 
        #   찾은 경우 중간 인덱스 반환
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return None



# n과 target을 입력
n, target = list(map(int,input().split()))
array = list(map(int,input().split()))

result = binary_re(array,target,0,n-1)
result2 = binary_for(array,target,0,n-1)
if result == None:
    print('원소가 존재 X')
else:
    print(result +1)


# 230720

# 부품 찾기
# 전자 매장에서 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
# 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다. 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램ㅇ르 작성하자

# 입력조건
# 첫째 줄에 정수 n이 주어진다.
# 둘째 줄에는 공백으로 구분하여 n개의 정수가 주어진다. 이때 정수는 1보다 크고 1000000이하이다.
# 셋째 줄에는 정수 m이 주어진다.
# 넷째 줄에는 공백으로 구분하여 m개의 정수가 주어진다. 이때 정수는 1보다 크고 1000000 이하이다.

# 출력조건
# ㅓㅅ째 줄에 공백으로 구분하여 각 부품이 존재하면 yse, 없으면 no
import sys
n = int(sys.stdin.readline().rstrip())
nA = sorted(list(map(int,sys.stdin.readline().rstrip().split())))
m = int(sys.stdin.readline().rstrip())
mA = sorted(list(map(int,sys.stdin.readline().rstrip().split())))
print(n,nA,m, mA)
def binarySearch(array,target,start,end):
    while start <= end:
        mid = (start + end)  // 2 
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else :
            start = mid + 1
    return None

for i in mA:
    if (binarySearch(nA,i,0,len(nA)-1)) != None:
        print('yes',end=' ')
    else:
        print('no',end=' ')

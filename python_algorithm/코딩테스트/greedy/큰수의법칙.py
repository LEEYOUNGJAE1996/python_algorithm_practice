# 230707


#  큰 수로 이루어진 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M 번 더하여 가장 큰 수를 만드는 법칙이다. 
# 단, 배열의 특정한 인덱스 ( 번호)에 해당하는 수가 연속해서 K 번을 초과하여 더해질 수 없는 거ㅏㅅ이 이 법칙의 특징이다.

# N = list(map(int,input().split()))
# M = int(input())
# K = int(input())
# maxSum = 0
# maxNumber = max(N)
# if N.count(maxNumber) > 1:
#     maxSum = maxNumber * M 
# else :
#     N.pop(maxNumber)
#     next = max(N)
#     for i in range(1, M):
#         if (i % 4) == 0 :
#             maxSum += next
#         else :
#             maxSum += maxNumber
# print(maxSum)


# 답안 

# N, M, K 공백 입력 받기 
n, m, k = map(int,input().split())
data = list(map(int,input().split()))

data.sort() #입력받은 수 정렬
first = data[n-1]
second = data[n-2]
sum = 0
for i in range(1,m+1):
    if i % (k+1) == 0 :
        sum += second
    else:
        sum += first
print(sum)
# 230802

#볼링공 고르기
# A, B 두 사람이 볼링르 치고 있습니다. 두 사람은 서로 무게가 다른 볼링공을 고르려고 한다.
# 볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀있다.
# N개의 공의 무게가 각각 주어질 때 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램

# 입력 조건
# 첫째 줄에 볼링공의 개수 N 공의 최대 무게 M이 공백으로 구분되어 각각 자연수 형태로 주어진다.
# 둘째 줄에 각 볼링공의 무게 K 공백으로 구분되어 순서대로 자연수 형태로 주어진다.

# 출력 조건
# 첫째 줄에 두 사람이 볼링공을 고르는 경우의 수를 출력합니다.


# 단. 같은 무게의 공이 여러개 있을 수 있지만 서로 다른 공으로 존재


# n, m = map(int,input().split())
# ballWeights = list(map(int,input().split()))
# ballWeights.sort()

# count = 0 
# for ballWeight in ballWeights:
#     previous = ballWeight
#     for ballWeight in ballWeights:
#         if previous != ballWeight:
#             count +=1

# print(count)

# 문제 해설
# 이 문제를 효과적으로 해결하기 위해서는 먼저 무게마다 볼리공이 몇 개 있는지를 계산해야 한다.

n , m  = map(int,input().split())
data = list(map(int,input().split()))

countBallWeights = [0] * 11
for x in data:
    countBallWeights[x] += 1 

result = 0
for i in range(1,m+1):
    n -= countBallWeights[i]
    result += countBallWeights[i] * n

print(result)

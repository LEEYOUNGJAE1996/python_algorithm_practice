# 0725

# 미래도시
# 프로이드 워셜 알고리즘 적용?

# 문제 해설
# n의 범위가 100이하로 매우 한정적 프로인드 워셜 알고리즘ㅇ르 이용해도 빠르게 풀 수 있다.

INF = int(1e9)

# 노드의 개수 및 간선의 개수
n , m = map(int,input().split())
# 2차원 리스트
graph = [[INF] * n+1 for i in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b :
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1


# 거쳐 갈 노드 x와 최종 목적지 노드 K를 입력받기
x, k = map(int, input().split())


# 거리 확인하기 
for j in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][j] + graph[j][b])

# 수행된 결과를 출력하기
distance = graph[1][x] + graph[x][k]

if distance != INF:
    print(distance)
else:
    print(-1)


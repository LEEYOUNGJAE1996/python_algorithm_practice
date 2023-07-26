# 0725

# 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우


# 단께마다 거쳐 가는 노드를 기준으로 알고리즘을 수행한다.
# 하지만 매번 방문하지 않은 노드 중에ㅓㅅ 최단 거리를 갖는 노드를 찾을 필요가 없다는 점이 다르다.

# 2차원으로 표현
# 경유


# 무한의 의미를 가지는 값
INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값ㅇ르 무한으로 초기화\
graph = [[INF] * n+1 for i in range(n+1)]

# 자기 자신에게 자기 자신으로 가는 경우 비용은 0으로
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 , 그 값을 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C 라고 설정
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 위셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a,b], graph[a][k]+graph[k][b])
for a in range(1, n+1):
    for b in range(1,n+1):
        #도달할 수 없는 경우, 무한이라고 출력
        if graph[a][b] == INF:
            print("INFINITY",end = " ")
        else :
            print(graph[a][b],end=" ")
# 0725

# 힙 자료구조를 사용

# 힙 설명
# 힙 자료구조 - 우선순위 큐를 구현하기 위하여 사용하는 자료구조 중 하나

# 한 지점에서 다른 특정 지점까지의 최단 경로를 구하는 경우

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) #무한을 의미하는 값으로 10억을 지정

# 노드의 개수, 간선의 개수 입력

n,m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기

for dis in range(m):
    a,b,c = map(int,input().split())
    # a번 노드에서 b번노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q : # 큐가 비어있지 않다면
        # 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist :
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now] :
            cost = dist + i[1]
            # 현재 노드를 거쳐서 ,다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거릴르 출력
for i in range(1,n+1):
    # 도달할 수 없느 ㄴ경우, 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

print()
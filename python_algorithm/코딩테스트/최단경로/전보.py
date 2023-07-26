# 0725

# 전보

# 다익 

# 문제해설

# 이 문제를 들여다 보면 한 도시에서 다른 도시까지의 최단 거리 문제로 치환 가능
# 다익스트라 알고리즘 이용
# n과 M의 범위가 충분히 크기 때문에 우선순위 큐를 사용

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수 , 간선의 개수 , 시작 노드를 입력 받기
n,m,start = map(int,input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for  i in range(n+1)]
# 최단 거리 테이블
distance = [INF] * (n+1)

# 모든 간선 정보 입력 받기
for j in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))


def dijk(start):
    # queue
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + distance[i[1]]
            # now 에서 i[1]로 이동할 때 거리가 더 큰 경우
            if distance[i[1]] < cost:
                distance[i[0]]= cost


dijk(start)
# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에ㅓㅅ, 가장 멀리 있는 노드와의 최단 거리
max_distance =  0
for d in distance:
    # 도달할 수 있는 노드의 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance,d)

print(count-1,max_distance)

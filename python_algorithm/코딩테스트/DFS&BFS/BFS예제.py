# 230718

# BFS를 구현한다.

from collections import deque

def bfs(graph, start, visited):
    # 큐 구현을 위해  deque 라이브러리를 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v,end=" ")
        # 해당 원소와 연결된, 아직 방문하지 않은 노드를 큐에 넣는다.
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 각 노드가 연결된 정보를 리스트 자료형으로 표현*(2차원 리스트)
graph = [ [],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
# 각 노드가 방문된 정보를 리스트 자료형을 표현 (1차원 리스트)
visited = [False for i in range(9)]

start = 1
# bfs 테스트
if __name__== "__main__":
    bfs(graph, start, visited)


#  중요포인트는 DFS와 유사하지만 처음에 queue에 시작 노드를 넣고 노드를 시작을 인접한 노드를 찾는다는 것이다. 
#  이를 위해 큐의 첫번째 노드를 가져오고 그 노드와 연결된 노드를 for 을 통해 queue에 넣는 것이다. 
#  
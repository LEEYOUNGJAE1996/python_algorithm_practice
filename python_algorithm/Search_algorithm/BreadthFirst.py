# 너비 우선 탐색 프로그램
# 깊이 우선 탐색과 유사 그러나 노드를 따라 계속 이동하는 것이 아닌
# 기준이 되는 노드를 기준으로 연결된 노드를 우선 탐색하고 그 이후
# 탐색하지 못한 경우 자식노드의 자식 노드를 같은 방식으로  탐색


# 깊이 우선 탐색 기법과 같은 그래프 사용
graph = {
    'a': ['b', 'c'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'f'],
    'd': ['b'],
    'e': ['b', 'f'],
    'f': ['c', 'e']
}

# 너비 우선 탐색 함수 정의


def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        # 현재 큐에 입력된 노드 확인
        print('현재 큐 : ', queue)
        node = queue.pop(0)
        # 방문을 이미 했던 곳일 경우 지나치는 경우
        if node not in visited:
            print('현재 노드 위치 : ', node)
            visited.add(node)
            # 기준이 된 노드의 근처의 노드를 큐에 넣어주는 역할
            for neighbor in graph[node]:
                queue.append(neighbor)


bfs(graph, 'a')

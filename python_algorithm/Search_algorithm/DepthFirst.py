# 깊이 우선 탐색 방법으로 stakc을 이용하여 탐색한다.
# 이 때 탐색 할 때 비선형 구조인 되어있는 경우 갔던 지점들은 갔음을 표시하고
# 자손 노드쪽으로 계속 이동하며 탐색한다.

# 트리 형태 구현
graph = {
    'a': ['b', 'c'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'f'],
    'd': ['b'],
    'e': ['b', 'f'],
    'f': ['c', 'e']
}

# DFS 구현 함수


def dfs(graph, node, visited):
    # 방문한 곳이 아니면 해당 노드에 방문했음을 표시
    if node not in visited:
        print(node)
        visited.add(node)
        # 방문한 노드의 자식 노드로 이동
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


# a를 시작으로 탐색
visited = set()
dfs(graph, 'a', visited)

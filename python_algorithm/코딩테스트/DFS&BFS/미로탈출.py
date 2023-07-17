# 230718

# 미로 탈출 예제

# 1,1 위치에서 n,m 위치의 출구로 이동한다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시한다. 미로는 반드시 탈출할 수 있는 형태로 되어 있다.


# BFS로 풀면 되겠군

# 입력조건 
# 첫째 줄에 두 정수 n, m이 주어진다. 다음 n개의 줄에는 각각 m개의 정수로 미로의 정보가 주어진다.
# 각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.

# 출력 조건 첫째 줄에 최소 이동 칸의 개수를 출력한다.



############################################################################################################################
# 이를 위해 해당 거리까지 지나온 경로를 계속 카운트 한다. 이동 결과 원하는 위치까지 가지 않고 이전에 노드로 돌아오는 경우 -1을 한다.

# from collections import deque
# n , m= map(int,input().split())
# graph = [list(map(int,input())) for i in range(n)]
# dx = [1,-1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y):
#     queue = deque([])
#     queue.append([x,y])
#     count = 1
#     # 출구까지 이동하기 전까지 반복
#     while not(x == n-1 and y == m-1):
#         # 현재 위치에서 이동이 가능한 최근을 파악한다.
        
#         now = queue.popleft()

#         print(now)
#         count -=1
#         x = now[0]
#         y = now[1]
#         for i in range(4):
#             # 상하좌우 이동을 구현
#             ndx = x + dx[i]
#             ndy = y + dy[i]
#             count +=1
#             # 해당 범위를 넘어가는 경우
#             if ndx < 0 or ndx >= n or ndy <0 or ndy >= m or graph[ndx][ndy] != 1:
#                 count -=1
#             elif graph[ndx][ndy] == 1:
#                 queue.append([ndx,ndy])
#     return count

# print(bfs(0,0))


# 문제 최소를 탐색하는 방법에서 막힘

############################################################################################################################


# 문제 해설
# BFS를 이용했을 때 매우 효과적으로 해결이 가능
# BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문이다. 그러므로 (1,1) 지점에서부터 BFS를 수행하여 모든 노드의 값을 거리 정보로 넣으면 된다.
# 특정한 노드를 방문하면 그 이전 노드의 거리에 1을 더한 값을 리스트에 넣는다. 


# 문제 풀이 코드

from collections import deque

# n, m  입력
n, m = map(int,input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = [list(map(int,input())) for i in range(n)]


# 이동할 네 방향 정의 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 소스 코드 구현
def bfs(x,y):
    #  큐 구현을 위한 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    while queue: # 이 부분이 문제였다. 해당 문제를 푸는 것이 목적이 아닌 queue가 빌 때까지 반복하는 것을 목표로 한다.
        x,y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 넘어가는 경우
            if nx < 0 or nx >=n or ny < 0 or ny >=m :
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0 :
                continue
            #  해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 ######## key point 이동할 때마다 +1을 해서 그래프에 해당 위치까지 얼마나 이동한 것인지 표시
                queue.append((nx,ny))
    #가장 오른쪽 아래까지의 최단 거리 반환
    print(graph)
    return graph[n-1][m-1]

print(bfs(0,0))


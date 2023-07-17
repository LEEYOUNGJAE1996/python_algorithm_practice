# 230718

# 음료수 얼려먹기

# N*M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재한느 부분은 1로 표시된다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙이 있는 경우 서로 연결되어 있는 것을 간주한다.
# 이때 얼음 ㅌ르의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오


# 입력 조건
# 첫 번째 줄에 틀의 세로 길이 N과 가로 길이 M이 주어진다.
# 두 번쨰 줄부터 N+1 번째 줄까지 얼음 틀의 형태가 주어진다.
# 이때 굼어이 뚫려있는 부분은 0 , 그렇지 않은 부분은 1이다. 


# 출력 조건 : 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.


################################################################################################################################
# from collections import deque


# n, m = map(int,input().split())
# # 무엇을 구해야하는가 - 연결된 정도를 파악한다. 이를 위해서는 해당 입력을 그래프 형태로 만든다. 
# # visited == 0 인 구간을 false 로 1인 구간을 true로 둔다.
# # 해당 방법을 활용하여 bfs를 구현한다.
# # start는 처음 graph에서 해당 행에서 처음 false인 index를 찾는다. 이후에 bfs를 돌린다
# # bfs를 돌린 이후 다시 한 번 해당 행을 주축으로 false인 구간을 찾는다. 
# # 해당 행이 true 인 경우 다음 행으로 넘어간다. n행이 될 때까지 전부 수행한다.

# # 상하좌우 이동
# dx = [0,0,-1,1]
# dy = [1,-1,0,0]
# bottle = []
# graph = [[[] for i in range(m)] for i in range(n+1)]
# visited = [ [False for i in range(m)] for i in range(n+1)]
# for i in range(n):
#     bottle.append(input())
# x , y = 0,0

# # 그래프를 그린다. 
# # 상하좌우 이동이 가능하므로 이를 토대로 연결된 노드를 찾는다.
# # 해당 노드의 값이 
# for i in bottle:
#     y +=1
#     x= 0
#     for letter in i:
#         x += 1
#         if letter == '0':
#             print('letter is 0')
#             for move in range(4):
#                 ndy = y + dy[move]
#                 ndx = x + dx[move]
#                 print(f'y : {y},x : {x},ndy : {ndy},ndx : {ndx}')
#                 if ndy > 1 and ndy < n+1 and ndx > 1 and ndx < m+1:
#                     if bottle[ndy-1][ndx-1] == '0':
#                         graph[y][x-1].append((ndy,ndx))

#         else :
#             visited[y][x-1] = True
# print(bottle)
# print(graph)
# print(visited)

# 그래프부터 막힌다. 어떻게 구현을 해야하는가?


################################################################################################################################
# 위의 과정은 나의 풀이 과정 - but 30분이란 시간 내에 풀지 못해 아래의 답을 적어본다.


# 문제 해설 
# 이 문제는 DFS로 해결할 수 있다. 일 단 앞에서 배운대로 얼음을 얼릴 수 있는 공간이 상하좌우로 연결되어 있다고 표현할 수 있으므로 그래프 형태로 모델링 할 수 있다.
# 1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 주엥서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다.
# 2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 다시 진행하면, 연결된 모든 지점을 방문할 수 있다.
# 3. 1~2번의 과정ㅇ르 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다.


n, m = map(int,input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        #  해당 노드 방문 처리
        graph[x][y] = 1
        #  상하좌우의 위치도 모두 재귀적으로 호출
        print(graph)
        dfs(x -1, y)
        dfs(x , y-1)
        dfs(x +1, y)
        dfs(x , y +1)
        return True
    return False

# 모든 노드에 대하여 음료수 채우기ㅣ
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result +=1 

print(result)

# 나의 문제점 DFS 가 탐색 모델임을  그리고 visited를 어떻게 설정할 것이가 정하지를 못함
# 과거 구현에서 배운 dx dy 이동에 대한 지식의 저주에 걸림
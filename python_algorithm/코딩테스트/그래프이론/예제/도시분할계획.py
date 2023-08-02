# 230801

# 도시 분할 계획

#  마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다.
#  마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야 한다.


# 첫째 줄에 집의 개수 n 길의 개수 m이 주어진다.
# 그다음 줄부터 m줄에 걸쳐 길의 정보가 abc 3개의 정수로 공백으로 구분되어 주어지는데 a번 집과 b번 집을 연결하는 길의 유지비가 c라는 뜻이다.

# 출력 조건 : 첫째 줄에 길을 없애고 남은 유지비 합의 최솟값ㅇ르 출력한다.


# 서로소 및 cycle 제거 

# 크루스칼 알고리즘으로 최소 신장 트리를 찾은 뒤에 최소 신장 트리를 구성하는 간선 중에서 큰 간선ㅇ을 제거하는 것 
# 

# parent node 찾기
def findParent(parent, node):
    if parent[node] != node:
        parent[node] = findParent(parent,parent[node])
    return parent[node]

# node의 루트 노드 즉 parent 합치기
def unionParent(parent, firstNode, secondNode):
    firstNodeParent = findParent(parent,firstNode)
    secondNodeParent = findParent(parent, secondNode)
    if firstNodeParent < secondNodeParent:
        parent[secondNode] = firstNodeParent
    else:
        parent[firstNode] = secondNodeParent

v, e = map(int,input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

edges = []
result = 0

for i in range(1,v +1):
    parent[i] = i

for directionAndCostCount in range(e):
    firstNode, secondNode, cost = map(int,input().split())
    # 비용 순으로 정렬하기 위한 첫 번째 요소를 cost로 저장
    edges.append((cost,firstNode,secondNode))

edges.sort()
last  = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

# 하나씩 check
for edge in edges:
    cost , firstNode, secondNode = edge
    if findParent(parent,firstNode) != findParent(parent,secondNode):
        unionParent(parent, firstNode, secondNode)
        result += cost
        last = cost

print(result - last)

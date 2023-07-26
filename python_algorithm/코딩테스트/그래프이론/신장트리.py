# 0726

# 신장트리 : 하나ㅡ이 그래프가 있을 떄 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미하낟.
# 이때 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 성립 조건

# 크루스칼 알고리즘
# 최소 신장 트리 알고리즘


# 간선데이터를 비용에 따라 오름차순으로 정렬
# 간선ㅇ르 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
#   사이클이 발생하지 않는 경우 최소 신장 트리에 퐇마
#   사이클이 발생 최소 신장트리 제외
# 모든 간선에 대하여 위의 과정을 반복


# 특정 원소가 속한 집합을 찾기

def findParent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = findParent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def unionParent(parent,a,b):
    a = findParent(parent,a)
    b = findParent(parent,b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

# 노드의 개수가 간선(union 연산) 개수 입력받기
v, e = map(int,input().split())
parent = [0]* (v+1)


# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edge = []
result = 0


for i  in range(1,v+1):
    parent[i] = i

# 모든 간선에 대한 정보

for i in range(e):
    a,b,cost = map(int,input().split())
    # 비용순으로 정렬
    edge.append((cost,a,b))

# 간선을 비용순으로 정렬
edge.sort()


for ed in edge:
    cost,a,b = ed
    # 사이블이 발생하지 않는지 확인
    if findParent(parent, a) != findParent(parent,b):
        unionParent(parent,a,b)
        result += cost
        
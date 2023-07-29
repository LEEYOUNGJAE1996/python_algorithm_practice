# 0726

def findParent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x :
        return findParent(parent,parent[x])
    return x

# 두 원소가 속한 집합 합치기
def unionParent(parent,a,b):
    a = findParent(parent, b)
    b = findParent(parent, a)
    if a<b:
        parent[b] = a
    else :
        parent[a] = b

#노드의 개수와 간선의 개수 입력하기
v,e = map(int,input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 부모 테이블 상에서 , 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i


# 사이클 판별을 위한
cycle = False


# union 연산을 각각 수행
for i in range(e):
    a,b = map(int,input().split())
    if findParent(parent,a) == findParent(parent,b):
        cycle = True
        break
    else :
        unionParent(parent,a,b)


# 각 원소가 속한 집한 출력
print('각 원소가 속한 집합: ', end = '')
for i in range(1,v+1):

    print(findParent(parent,i), end=' ' )



# 부모 테이블 내용 출력

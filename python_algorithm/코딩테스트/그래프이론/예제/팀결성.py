# 230801

# 팀 결성

# 학교에서 학생들에게  0 번부터 N 번까지 부여
# 팀 N +1로 존재 이때 선생님은 팀 합치기 연산과 같은 같은 팀 여부 확인 연산 

# 1. 팀 합치기 연산은 두 팀을 합치는 연산이다.and
# 2. 같은 팀 여부 확인 연산은 특정한 두 학생이 같은 팀에 속하는지를 확인하는 연산

# 입력 조건
# 첫째 줄에 N, M이 주어진다. M 은 입력으로 주어지는 연산의 개수이다. 
# 다음 M 개의 줄에는 각각의 연산이 주어진다. 
# 팀 합치기 연산은 0 a b 형태로 주어진다. 이는 A 번 학생이 속한 팀과 b 번 학생이 속한 팀을 합친다는 의미이다.
# 같은 팀 확인 연산은 1 a b 형태로 주어진다. 이는 a번 학생이 속한 팀과 b 번 학생이 같은 팀에 속해 있는지를 확인하는 연산이다.
# a와 b는 N 이하의 양의 정수이다. 

# 출력 조건
# 같은 팀 여부 확인 연산에 대하여 한 불에 하나씩 Yes 혹은 No로 결과를 출력한다.


# 서로수 check를 하는 것


# 부모 찾기
def findParent(parent, now):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 반복
    if parent[now] != now:
        parent[now] = findParent(parent, parent[now])
    return parent[now]

# Union 합치기
def unionParent(parent, firstNode, secondNode):
    firstNode = findParent(parent, firstNode)
    secondNode = findParent(parent,secondNode)
    if firstNode < secondNode:
        parent[secondNode] = parent[firstNode]
    else:
        parent[firstNode] = parent[secondNode]

n, m = map(int,input().split())
parent = [0] * (n+1)
for i in range(0,n+1):
    parent[i] = i

# 각 연산을 하나씩 확인
for i in range(m):
    operation , firstNode, secondNode = map(int,input().split())
    # 합집합  0 또는 확인 1s
    if operation == 0 :
        unionParent(parent,firstNode,secondNode)
    else :
        firstNodeParent = findParent(parent,firstNode)
        secondNodeParent = findParent(parent, secondNode)
        if firstNodeParent == secondNodeParent:
            print("YES")
        else :
            print("NO")


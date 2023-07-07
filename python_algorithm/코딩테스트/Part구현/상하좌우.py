# 230707

# 여행가는 A는 N * N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 * 1 크기의 정사각형으로 나눠어져 있다.
# 가장 왼쪽 위 좌표는 1,1 가장 오른쪽 아래 n,n

n = int(input())
y , x = 1,1
move = list(input().split())
for turn in move:
    if y < n and turn == "D":
        y += 1
    elif y > 1 and turn == "U":
        y -= 1
    elif x < n and turn == "R":
        x += 1
    elif x > 1 and turn == "L":
        x -= 1 
print(y, x)

# 책의 답변

n = int(input())
x, y = 1,1
plans = input().split()
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx , ny
print(x, y)

# 아래의 코드가 더 좋은 이유


# 위에서는 'y'와 'x'라는 두개의 변수를 사용하여 상, 하, 좌, 우로 이동에서 가능한 위치를 구했습니다. 
# 그러나 상, 하, 좌, 우를 나타내는 문자열(turn)과 계산을 위해 사용한 'y'와 'x'를 일일이 매칭해주어야 했기 때문에, 
# 코드가 수정되기 어렵고, 코드의 가독성도 떨어졌습니다. 반면에, 아래의 코드에서는 리스트(dx, dy, move_types)를 사용하여 계산을 하였습니다. 
# 이 방법을 사용하면 필요한 "L','R','U','D"를 각각 매칭된 인덱스(0,1,2,3)와 함께 정리하고, 'dx', 'dy'를 사용하여 이동 방향에 대한 계산을 진행할 수 있습니다. 
# 이를 통해 코드를 간결하게 작성할 수 있고, 재사용성도 높아지는 장점이 있습니다. 
# 또한, 아래의 코드에서는 'nx'와 'ny' 변수를 대입하는 if문 수행이 각각 'move_types' 리스트에 있는 문자열을 매번 확인하는 것이 아니라, 실제 'turn' 변수와 함께 수행되므로 좀 더 효율적인 방법입니다.
#  시간 및 공간 복잡도면에서도 더욱 효율적입니다.
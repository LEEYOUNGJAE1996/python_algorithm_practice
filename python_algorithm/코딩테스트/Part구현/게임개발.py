# 230712

# 게임 개발 난이도 2 40분

#현민이는 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발 중이다.
# 캐릭터가 있는 장소는 1*1 크기의 정사각형으로 이뤄진 N* M 크기의 직사각형으로 각각의 칸은 육지 또는 바다이다. 
# 캐릭터는 동서남북 중 한 곳을 바라본다.

# 맵은 각 칸은 (A,B) 로 나타낼 수 있고 , A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다.
# 캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다.
# 매뉴얼
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 왼쪽 방향에 가보지 않은 칸이 없다면 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 단, 이떄 뒤쪽방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

# 출력하고자 하는 것
# 메뉴얼에 따라 캐릭터를 이동시킨 뒤에 캐릭터가 방문한 칸의 수를 출력하는 프로그램

# 어떻게 움직이라는 것인지 이해를 할 수 없는 문제 우선 구현을 한다.



# 방향에 대해서 지시하기 
def turnLeft(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction

# 이동하는 방식에 대한 이동한 칸을 계산하는 함수를 만든다.
def moveManual(x,y,direction,d,mapData):
    count  = 1
    turnTime = 0
    d[x][y] = 1
    # 북 동 남 서 
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while True:
        direction = turnLeft(direction)
        print(d)
        print(mapData)
        x = x + dx[direction]
        y = y + dy[direction]
        print(x,y,direction,d[x][y],mapData[x][y])
        if d[x][y] == 0 and mapData[x][y] == 0 :
            count += 1
            print(count)
            turnTime = 0
            # 내가 지나간 자리는 1로 표시한다.
            d[x][y] = 1
            continue
        else : 
            x -= dx[direction]
            y -= dy[direction]
            turnTime += 1
        
        # 4칸 전부 이동이 불가능한 경우 한 칸 뒤로 가서 한 번더 진행. 단 뒤로 가는 것이 불가능하다면 그 자리에서 멈춘다.
        if turnTime  == 4:
            x -= dx[direction]
            y -= dy[direction]
            if mapData[x][y] == 0 :
                turnTime = 0
            else :
                break
    return count

if __name__ == "__main__":
    

    n , m = map(int,input().split())
    # 실제로 이동한 맵을 표시하는 
    d = [[0]*m for i in range(n)]
    # 현재 캐릭터의 위치 및 방향 구하기
    x, y , direction = map(int,input().split())

    # 맵 입력 받기 
    mapData = []
    for i in range(n):
        mapData.append(list(map(int,input().split())))

    count =moveManual(x,y,direction,d,mapData)
    print(count)

    # 무슨 문제가 있는거지?
    # 아 0 이 육지였다.
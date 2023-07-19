array = [2,6,45,76,7,2,58,3,26,56]

for i in range(1, len(array)):
    for j in range(i,0,-1): # 인덱스  i 부터 1까지 감소하며 반복하는 문법이다.
        if array[j] < array[j-1] : # 한 칸씩 왼쪽으로 이동
            array[j] , array[j-1] = array[j-1], array[j] # 중요 포인트 처음부터 시작하면서 가장 작은 수를 왼쪽으로 계속 옮겨 주는 것이다.
        else : 
            break

print(array)

# 삽입 정렬의 시간 복잡도 O(N^2) 최선의 경우 O(N)
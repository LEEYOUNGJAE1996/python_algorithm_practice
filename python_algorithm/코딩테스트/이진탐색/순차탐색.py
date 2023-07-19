# 230720

# 순차 탐색 소스코드 구현
def sequential_search(n,target,array):
    # 각 원소를 하나씩 비교
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i+1# 현재의 위치 반환
print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열 입력하세요.")
input_data = input().split()
print(input_data)
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열 입력. 구분은 띄어쓰기 한 칸으로 진향")
array = input().split()
print(sequential_search(n=n,target=target,array=array))

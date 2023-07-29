# 0728

# 한 모험가 N 명 있습니다. 모험가 길드에서는 n 명의 모험가를 대상으로 'rhdvhehfmf cmrwjd

# 첫째 줄에 모험가의 수 n 이 주어진다. 1 < 100000<
# 둘째 ㅜㅈㄹ에 각 모험가의 공포도의 값을 n .이하의 자연수로 주어지며, 각 자연수는 공백으로 구분

# 출력 : 여행을 떠날 수 있는 그룹 수의 최댓값을 출력

# 해설 
# 일단 공포도를 기준으로 오름차순으로 정렬 하는 경우

# 항상 최소한의 모험가의 수만 포함하여 그룹을 결성하게 된다. 따라서 최대한 많은 그룹이 구성되는 방법이므로, 항상 최적의 해를 찾을 수 있따.

n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0

count = 0

for i in data:
    count += 1 
    if count >= i :
        result += 1
        count = 0
print(result)
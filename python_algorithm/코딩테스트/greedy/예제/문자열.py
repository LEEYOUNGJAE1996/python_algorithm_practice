# 0728

#  첫째 줄에 0 과 1로만 이루어진 문자열 S가 주어진다. S의 길이는 100만보다 작습니다.

# 출력 : 첫째 줄에 다솜이가 해야 하는 행동의 최소 횟수를 출력합니다.


data = input()


num0 = 0
num1 = 0
previous = ''
for letter in data:
    if letter  == '0' and letter != previous:
        num0 +=1
    elif letter == '1' and letter != previous:
        num1 += 1
result = max (num0,num1)
print(result)
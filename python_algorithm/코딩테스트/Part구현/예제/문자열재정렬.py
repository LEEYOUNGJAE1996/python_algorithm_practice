# 230808

# 문자열 재정렬

string = input()
alpabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

result = []
sum = 0
for letter in string:
    if letter in alpabet:
        result.append(letter)
    else:
        sum += int(letter)
result.sort()
# 틀린점 숫자가 없는 경우 더 할 수 없다.
if sum != 0:    
    result.append(sum)
result = ''.join(result)
print(result)
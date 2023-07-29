# 0728

# 첫쨰 줄에 여러 개 의 숫자로 구성된 하나의 문자열 s 가 주어진다.


# 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력한다.

data = input()
result = 0
for letter in data:
    number = int(letter)
    if number <= 1:
        result += number
    else :
        result *= number

print(result)
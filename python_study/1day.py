
# input 먼저 진행
# print will print the word "hello" and the user inputS
print("Hello " + input("what's your name?  ") + "!")

print(len(input()))

name = "LEE"

# 데이터 타입이 중요한 이유

num_char = len(input("what's your name?  "))

type(num_char)
new_num_char = str(num_char)
print("Hello " + new_num_char + "!!")

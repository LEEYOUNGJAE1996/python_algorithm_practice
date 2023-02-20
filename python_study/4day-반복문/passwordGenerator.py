# 비밀번호 생성기 만들기
# 미니 프로젝트 230220 ~ 230220
# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# 내 코드
password = ""
for count in range(0, nr_letters):
    password += letters[random.randint(0, 52)]
for count in range(0, nr_symbols):
    password += symbols[random.randint(0, 8)]
for count in range(0, nr_numbers):
    password += numbers[random.randint(0, 9)]
print(password)

# 강의 코드
password_lec = ""
for count in range(0, nr_letters):
    password_lec += random.choice(letters)
for count in range(0, nr_symbols):
    password_lec += random.choice(symbols)
for count in range(0, nr_numbers):
    password_lec += random.choice(numbers)
print(password_lec)


# random.choice( list 타입 변수)
# 리스트 항목에서 램덤으로 값을 선택
# 다른 것도 같을라나?

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_hard = ""
letter_count = 0
number_count = 0
symbol_count = 0
for count in range(0, nr_letters+nr_numbers+nr_symbols):
    while (True):
        index_choice = random.randint(1, 3)
        # letter index
        if index_choice == 1 and nr_letters > letter_count:
            password_hard += letters[random.randint(0, 52)]
            letter_count += 1
            break
        elif index_choice == 2 and nr_numbers > number_count:
            password_hard += numbers[random.randint(0, 9)]
            number_count += 1
            break
        elif index_choice == 3 and nr_symbols > symbol_count:
            password_hard += symbols[random.randint(0, 8)]
            symbol_count += 1
            break
print(password_hard)

# 강의 코드
password_list = []
for count in range(0, nr_letters):
    password_list.append(random.choice(letters))
for count in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for count in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
# How to shuffle the list?
# 구글 검색 -> how to change the order in a list python?
print(f"your password : {password_list}")
random.shuffle(password_list)
# . random.shuffle(x)
# This is used to shuffle the sequence in place. A sequence can be any list/tuple containing elements.
print(password_list)
# string으로 for구문으로 더해주기만 하면 완성
password_hard_lec = ""
for char in password_list:
    # 주의 char is not integer type data  list에서 하나의 값을 가지고 있는 형태
    password_hard_lec += char
print(f"your password : {password_hard_lec}")


# key point
# random 내의 모르는 메소드 활용 - random.choice() random.shuffle()
# print(f"{}") 형태 기억할 것

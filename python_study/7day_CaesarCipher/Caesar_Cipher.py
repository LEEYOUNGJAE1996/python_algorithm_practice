# 230223

# functions with more than 1 input
import math
import logo


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# 순서 상관 없이 함수 데이터 입력 및 사용하는 법
# # parameter 에 argument 직접 입력
# def function(a, b, c):
#     print(a)
#     print(b)
#     print(c)


# function(c=2, a=1, b=4)


# 내가 짠 함수 ############################################################
# def encrypt(text, shift):
#     encrypt_text = ""
#     for letter in text:
#         for i in range(len(alphabet)):
#             if letter == alphabet[i]:
#                 if i + shift > 25:
#                     encrypt_text += alphabet[i+shift - 26]
#                 else:
#                     encrypt_text += alphabet[i+shift]
#     print(f"plain_text = \"{text}\"")
#     print(f"shift = {shift}")
#     print(f"cipher_text = \"{encrypt_text}\"")


# def decrypt(text, shift):
#     decrypt_text = ""
#     for letter in text:
#         for i in range(len(alphabet)):
#             if letter == alphabet[i]:
#                 #  반성해야할 점 list의 경우 음수의 인덱스를 가질 수 있다.
#                 if i - shift < 0:
#                     decrypt_text -= alphabet[i - shift]
#                 else:
#                     decrypt_text -= alphabet[i-shift]
#     print(f"cipher_text = \"{decrypt_text}\"")
#     print(f"shift = {shift}")
#     print(f"plain_text = \"{text}\"")

##########################################################################
# 강의에서 보여준 함수


# def encrypt_lec(plain_text, shift_amount):
#     chipher_text = ""
#     for letter in plain_text:
#         # 특정 원소의 인덱스를 반환해주는 index 함수
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         # 문제를 발견 초과 범위
#         cipher_text += alphabet[new_position]
#     print(f"plain_text = \"{text}\"")
#     print(f"shift = {shift}")
#     print(f"The encoded text is {chipher_text}")


# def decrypt_lec(chiper_text, shift_amount):
#     plain_text = ""
#     for letter in plain_text:
#         # 특정 원소의 인덱스를 반환해주는 index 함수
#         position = alphabet.index(letter)
#         # list 음수 인덱스가 가능하다
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"cipher_text = \"{plain_text}\"")
#     print(f"shift = {shift}")
#     print(f"The decoded text is {plain_text}")
#######################################################

# 코드 줄이기 밖에 encode decode if문 없애고 def 합치기
# my
def ceasar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            new_position = (position + shift) % 26
            #  굳이 빼기로 비교를 할 필요 X
            #  나머지값을 통해...
            # if new_position > 25:
            #     new_position = position + shift - 26
            # else:
            #     new_position = position + shift
        elif cipher_direction == "decode":
            new_position = (position - shift) % 26
        else:
            print("Worng Value")
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")


logo.logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


repeat = True
repeat_2 = True
while repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text, shift, direction)

    answer = input("반복을 원하면  Y 그만이면 N를 입력하세요 >>").lower()
    while repeat_2:
        if answer == "n":
            repeat = False
            repeat_2 = False
        elif answer != "y":
            print("worng value")
        else:
            repeat_2 = False


# 주된 차이점 함수에 대해서 아는 것이 적다
# 파이썬에서 나왔던 함수에 대해서 따로 정리를 해야겠다.

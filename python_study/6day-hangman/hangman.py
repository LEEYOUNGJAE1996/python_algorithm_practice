# 행맨 미니 프로젝트
# 230222
import random
import hanman_logo
import hangman_wordlist as word_list
# 아스키아트 함수로 정의


def graph(life):
    ascii_graph = ""
    if life == 5:
        ascii_graph = ''' +---+
  |   |
  O   |
      |
      |
      |
========= '''
    elif life == 4:
        ascii_graph = ''' +---+
  |   |
  O   |
 /    |
      |
      |
========= '''

    elif life == 3:
        ascii_graph = ''' +---+
  |   |
  O   |
 /|   |
      |
      |
========= '''

    elif life == 2:
        ascii_graph = ''' +---+
  |   |
  O   |
 /|\\  |
      |
      |
========= '''
    elif life == 1:
        ascii_graph = ''' +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
========= '''

    else:
        ascii_graph = ''' +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========= '''
    return ascii_graph


# Step 2
print(hanman_logo.logo)
chosen_word = random.choice(word_list.word_list)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

# 정답을 넣기 위한 글자 수 만큼 리스트로 만드는 과정
user_answer = []
for letter in chosen_word:
    user_answer.append('_')
print(user_answer)
life = 5


while life != 0:
    print(f"your life  >> {life}")
    print(graph(life))

    guess = input("Guess a letter: ").lower()
    correct = False

    # 정답이 리스트 화 되었는지 확인하는 코드

    # answer = []
    # for letter in chosen_word:
    #     answer.append(letter)

    # print(answer)

    # 비교하기 위한 값 비교
    i = 0

    for letter in chosen_word:
        if letter == guess:
            # 중복 비교 제거 + 중복 비교 하는 경우 목숨  -
            # 내가 구현한 코드
            # if user_answer[i] == letter:
            #     print("you already done!")
            #     continue
            # else:
            #     user_answer[i] = letter
            #     correct = True
            #  강의에서 제공하는 차이점!
            #  if문에서도 in 문을 써서 각 내용을 비교 할 수 있다.
            if guess in user_answer:
                print("you already done!")
                continue
            else:
                user_answer[i] = letter
                correct = True
        i += 1

    # 틀렸을 경우 목숨을 하나씩 줄이는 코드
    if correct == False:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        life -= 1

    print(user_answer)

    # 정답을 다 맞췄는지 비교하는 코드
    # 내가 구상한 코드
    # str_answer = ""
    # for letter in user_answer:
    #     str_answer += letter
    # if str_answer == chosen_word:
    #     print("You Win! ")
    #     break
    # 강의에서 나온 코드  in 이라는 구문을 이용해 좀더 깔끔한 코드를 구성
    if "_" not in user_answer:
        print("You win.")
        break
# 목숨이 다 소진한 경우 == 진경우
if life == 0:
    print(graph(life))
    print("You Lose!")
print("Game Over")


# 강의에서 제공하는 결과물

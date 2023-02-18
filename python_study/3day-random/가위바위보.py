import random as rd
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# 가위바위보 선택된 것을 아스키코드 아트로 보여주는 함수


def print_graph(choice_num, computer_choice, choice):
    print("computer choice")
    print(choice[computer_choice])
    print("your choice")
    print(choice[choice_num])


# Write your code below this line 👇
print("rock : 1 / scissors : 2 / paper : 3")
choice = [rock, scissors, paper]
choice_num = int(input("Enter your choice number >>"))-1
computer_choice = rd.randint(0, 2)
if choice == computer_choice:
    print_graph(choice_num, computer_choice, choice)
    print("draw")
elif choice_num == 0:
    if computer_choice == 1:
        print_graph(choice_num, computer_choice, choice)
        print("You Win!!!!!!!!!!")
    elif computer_choice == 2:
        print_graph(choice_num, computer_choice, choice)
        print("You Lose!!!!!!!")
elif choice_num == 1:
    if computer_choice == 2:
        print_graph(choice_num, computer_choice, choice)
        print("You Win!!!!!!!!!!")
    elif computer_choice == 0:
        print_graph(choice_num, computer_choice, choice)
        print("You Lose!!!!!!!")
elif choice_num == 2:
    if computer_choice == 0:
        print_graph(choice_num, computer_choice, choice)
        print("You Win!!!!!!!!!!")
    elif computer_choice == 1:
        print_graph(choice_num, computer_choice, choice)
        print("You Lose!!!!!!!")
else:
    print("잘못입력했습니다.")

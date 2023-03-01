# 230302

# 블랙잭 게임의 규칙
# 게임의 목표는 21에 가까운 숫자를 가지는 것이다.
# 21을 넘어가는 경우 진다.
# 처음에는 2장의 값을 가진다.
# 사용자가 더 카드를 받을 것인지 받지 않을 것인지 선택한다.
# 상대방과 비교하여 더 21에 가까운 사람이 승리한다.
# k j q 같이 특수한 카드의 경우에는 10으로 값을 고정한다.
# A의 카드의 경우에는 자신에 상황에 맞춰서 1 또는 11 로 계산한다.


# 내가 만드는 블랙잭 코드
import random as rd
import art

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def cal_cardsum(card_list):
    sum = 0
    card_list = sorted(card_list)
    for i in card_list:
        if sum+i >= 21 and i == 11:
            i = 1
        sum += i
    return sum


def print_card(user, computer):
    print(f"your card : {user}")
    print(f"computer card : {computer[0]}")


def card_comparison(user, computer):
    if cal_cardsum(user) > 21 and cal_cardsum(computer) > 21:
        return "Draw"
    elif cal_cardsum(user) > 21 and cal_cardsum(computer) <= 21:
        return "You Lose!"
    elif cal_cardsum(user) <= 21 and cal_cardsum(computer) > 21:
        return "You Win!"
    elif 21-cal_cardsum(user) < 21-cal_cardsum(computer):
        return "You Win!"
    elif 21-cal_cardsum(user) > 21-cal_cardsum(computer):
        return "You Lose!"
    else:
        return "Draw"


def new_stop():
    choice = input("계속하고 싶다면 'y' 그만하고 싶다면 'n' >> ").lower()
    if choice == 'y':
        return True
    elif choice == 'n':
        return False
    else:
        print("you enter worng value. system out")
        return False


def game_start():
    new_game = True
    while new_game:
        print("게임을 시작하겠습니다.")
        user_card = []
        com_card = []
        add_card = True
        user_card.append(card[rd.randint(0, 12)])
        user_card.append(card[rd.randint(0, 12)])
        com_card.append(card[rd.randint(0, 12)])
        # user card
        while add_card:
            print_card(user_card, com_card)
            # 카드를 더 받을 것인지 확인하는 공간
            choice = input("카드를 더 받고 싶다면 'y' 그만 받고 싶다면 'n'를 입력 >> ").lower()
            if choice == 'y':
                user_card.append(card[rd.randint(0, 12)])
                if cal_cardsum(user_card) > 21:
                    print("bust")
                    add_card = False
            elif choice == 'n':
                add_card = False
            else:
                print("You enter worng value")
        # computer version
        add_card = True
        while add_card:
            if cal_cardsum(com_card) < 13:
                com_card.append(card[rd.randint(0, 12)])
            elif cal_cardsum(com_card) >= 13 and cal_cardsum(com_card) <= 15:
                choice_com = rd.randint(0, 1)
                if choice_com == 0:
                    add_card = False
                else:
                    com_card.append(card[rd.randint(0, 12)])
            else:
                add_card = False
        print(user_card)
        print(com_card)
        print(card_comparison(user=user_card, computer=com_card))
        new_game = new_stop()


print(art.logo)
game_start()
print("게임을 종료합니다.")


# list 총 합을 더해주는 sum 이라는 함수가 이미 존재
# list에서 특정 값을 찾아 제거하는 함수 remove가 존재
# list를 다루는 함수들에 대해서 공부할 필요가 있음을 인지

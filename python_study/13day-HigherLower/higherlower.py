# 230305


# 1. 데이터 가져오기

import data
import art
import random as rd


def play_game():
    # 2 . 로고 보여주고 문제 출력하기
    print(art.logo)
    print("게임을 시작합니다. 다음에 제시되는 선택지 중에 팔로워 수가 더 많은 사람을 선택하면 됩니다.")
    print("\n\n\n")
    count = 0
    # 나왔던 문제가 다시 나오는 경우 다시 문제 뽑기
    already = []

    # 정답을 맞추는 경우 게임 지속 아님 게임 끝
    game_continue = True

    while game_continue:
        print(f"현재까지 맞춘 점수 : {count}")
    # 나왔던 문제가 다시 나오는 경우 다시 문제 뽑기
        # A의 경우
        new_item_A = True
        while new_item_A:
            A = data.data[rd.randrange(0, len(data.data)-1)]
            if already == []:
                already.append(A)
            else:
                for i in already:
                    if i == A:
                        new_item_A = True
                        break
                    else:
                        new_item_A = False
                if new_item_A == False:
                    already.append(A)
        # B의 경우
        new_item_B = True
        while new_item_B:
            B = data.data[rd.randrange(0, len(data.data)-1)]
            for i in already:
                if i == B:
                    new_item_B = True
                    break
                else:
                    new_item_B = False
            if new_item_B == False:
                already.append(B)

        print(f"A. ", end="")
        print(A["name"])
        print(art.vs)
        print(f"B. ", end="")
        print(B["name"])

        user_answer = input(
            "누가 더 팔로워가 더 많은가? ('A' or 'B' 로 입력해주세요) >> ").upper()

        # user가 A를 선택한 경우와 B를 선택한 경우로 나눠서 진행
        if user_answer == "A":
            if A["follower_count"] > B["follower_count"]:
                count += 1
            else:
                # 게임 종료 표시
                game_continue = False
        elif user_answer == "B":
            if A["follower_count"] < B["follower_count"]:
                count += 1
            else:
                # 게임 종료 표시
                game_continue = False
        else:
            print("You enter the worng value. system out")
            # 게임 종료
            game_continue = False
        print(
            f"{A['name']} : {A['follower_count']}  vs {B['name']} : {B['follower_count']}\n\n\n")

    # 게임이 종료된 경우\
    print(f"지금까지 총 {count}개를 맞췄습니다.")


# 게임을 계속할건지 말건지!
new_game = True
while new_game:
    play_game()
    wantIt = True
    while wantIt:
        new_want = input(
            "게임을 계속하시겠습니까? (계속을 원하는 경우 'T' 그만하기를 원하는 경우 'S'를 입력해주세요)>> ").upper()
        if new_want == "S":
            new_game = False
            wantIt = False
        elif new_want == "T":
            print("\n\n\n\n\n새로운 게임을 시작합니다.")
            wantIt = False
        else:
            print("잘못된 값을 입력하셨습니다. 다시 작성해주세요.")

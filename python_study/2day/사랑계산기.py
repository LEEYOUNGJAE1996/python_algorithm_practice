# 영어 이름을 입력해서 이름에 T,R,U,E 가 있으면 10단위에
#  L, O, V, E가 있는 수만큼 에 1의 자리에 가산한다. 최종 결과를 퍼센트로 출력한다.
# 이 때 대문자 또는 소문자를 각각 처리하기 힘들기에
# .lower() 또는 .upper() 함수를 사용한다.
# 또한 글자 수를 세기 위한 함수 .count("찾고자 하는 문자열")을 사용해서 갯수를 구한다.

name1 = input("enter the  your name >> ").lower()
name2 = input("enter the thier name >> ").lower()
name = name1 + name2
count_t = name.count("t")
count_r = name.count("r")
count_u = name.count("u")
count_e = name.count("e")
count_l = name.count("l")
count_o = name.count("o")
count_v = name.count("v")

true_love = (count_t+count_r+count_u +
             count_e)*10 + count_l+count_o+count_v+count_e
if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, 잘해봐")
elif true_love > 60:
    print(f"Your score is {true_love}, 응원해")
else:
    print(f"Your score is {true_love}, 포기해")

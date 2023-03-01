# 230301


# 첫 번째 글자만 대문자로 만들기
def format_name(names):
    after_name = ""
    # split으로 나눠 리스트 형태로 존재하기 떄문에 이와 같이 비교를 해야한다.
    if names == []:
        return "you enter worng value."
    else:
        for name in names:
            f_name = name[0]
            l_name = name[1:]
            after_name += f_name.upper() + l_name.lower() + " "
        return after_name


name = input("enter name >>").split()

print(format_name(name))

# 강의를 본 뒤...
# 이미 title 이란 함수가 존재
print(input("enter name >> ").title())

# 230309

from turtle import Turtle, Screen

young = Turtle()
screen = Screen()


def move_forwards():
    young.forward(10)


screen.listen()
# space키를 누르면 , 뒤에 구문을 실행
# 주의 fun에 입력하는 경우 함수의 ()를 입력하면 받아들이지 못함
# ()를 제외한 상태로 입력
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()

# 함수를 input으로


# def func_a(something):
#     print(something())


# def func_c(something):
#     print(something)


# def func_b():
#     return "hello world"


# func_a(func_b)
# func_c(func_b)

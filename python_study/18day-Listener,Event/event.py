# 230309

from turtle import Turtle, Screen

young = Turtle()
screen = Screen()
young.color("violet")
young.pensize("3")
young.shape("turtle")


def move_forwards():
    young.forward(10)


def move_backwards():
    young.backward(10)


def move_clockwise():
    young.right(10)


def move_counter_clock():
    young.left(10)


def move_clear():
    young.clear()
    young.penup()
    young.home()
    young.pendown()


screen.listen()
# space키를 누르면 , 뒤에 구문을 실행
# 주의 fun에 입력하는 경우 함수의 ()를 입력하면 받아들이지 못함
# ()를 제외한 상태로 입력
screen.onkey(key="space", fun=move_forwards)
# TODO another movement
# w : forward
screen.onkey(key="w", fun=move_forwards)
# s : backward
screen.onkey(key="a", fun=move_counter_clock)
# d : clockwise
screen.onkey(key="s", fun=move_backwards)
# a : counter-clockwise
screen.onkey(key="d", fun=move_clockwise)
# c: clear drawing
screen.onkey(key="c", fun=move_clear)


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

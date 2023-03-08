import turtle
import random as rd


def random_color():
    R = (rd.randrange(160, 255))
    G = (rd.randrange(160, 255))
    B = (rd.randrange(160, 255))
    color_tuple = (R, G, B)
    return color_tuple


tur = turtle.Turtle()
tur.shape("turtle")
tur.pensize(2)
tur.speed("fastest")
# RGB 형태로 색을 지정하기 위해 따로 모드를 지정할 필요가 있다.
# 주의할 점 클래스에 있는 것이 아는 turtle 모듈에 존재 so 따로 import를
# 이번에는 모듈 자체를 import
turtle.colormode(255)
for i in range(100):
    tur.color(random_color())
    tur.circle(radius=100)
    tur.left(3.6)

### This code will not work in repl.it as there is no access to the colorgram package here.###
## We talk about this in the video tutorials##
import random as rd
import turtle
import colorgram

rgb_colors = []
colors = colorgram.extract(
    'D:\\workstation\\python_algorithm_practice\\python_study\\17day-turtle&GUI\\hirst-painting-start\\image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)


# 230308


tur = turtle.Turtle()
tur.shape("turtle")
tur.pensize(2)
tur.speed("fastest")
# RGB 형태로 색을 지정하기 위해 따로 모드를 지정할 필요가 있다.
# 주의할 점 클래스에 있는 것이 아는 turtle 모듈에 존재 so 따로 import를
# 이번에는 모듈 자체를 import
turtle.colormode(255)
for i in range(10):
    for i in range(10):
        tur.color(rgb_colors[rd.randrange(0, 29)])
        tur.dot()
        tur.penup()
        tur.forward(10)
    tur.backward(100)
    tur.left(90)
    tur.forward(10)
    tur.right(90)

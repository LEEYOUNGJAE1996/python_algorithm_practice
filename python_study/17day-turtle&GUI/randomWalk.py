import color_list
from turtle import Turtle
import random as rd
timmy_turtle = Turtle()
# 지나가는 선의 굵기 지정
timmy_turtle.pensize(5)
# 지나가는 커서의 모양을 지정
timmy_turtle.shape("turtle")
# 커서의 이동 속도를 지정
timmy_turtle.speed(10)
for i in range(100):
    # 선의 색을 지정
    timmy_turtle.color(rd.choice(color_list.color_list))
    timmy_turtle.forward(50)
    # 4방향 0 90 180 270 중 한 방향을 랜덤으로 지정
    choice = rd.randrange(1, 4)
    timmy_turtle.right(choice*90)

from turtle import Turtle
import random as rd

# Food 클래스에서 Turtle의 모든 기능을 상속 받으려고 한다.


class Food(Turtle):
    def __init__(self):
        super().__init__()
        # Turtle 클래스의 기능을 상속 받았기에 가능한 self
        self.shape("circle")
        self.penup()
        # 터틀의 기본 크기 20* 20
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")
        random_x, random_y = rd.randint(-280, 280)//10 * \
            10, rd.randint(-280, 280)//10*10
        self.goto(random_x, random_y)

    # food 새로운 위치에 생성
    def newFood(self):
        random_x, random_y = rd.randint(-280, 280)//10 * \
            10, rd.randint(-280, 280)//10*10
        self.goto(random_x, random_y)

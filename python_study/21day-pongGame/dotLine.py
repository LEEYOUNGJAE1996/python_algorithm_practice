from turtle import Turtle


class DotLine():
    def __init__(self):
        self.dotLine = []
        for i in range(-300, 300, 10):
            dot_part = Turtle()
            dot_part.penup()
            dot_part.shape("square")
            dot_part.color("white")
            dot_part.shapesize(stretch_wid=0.25)
            dot_part.goto(0, i)
            self.dotLine.append(dot_part)

    def __del__(self):
        print(self.dotLine)
        for i in range(len(self.dotLine)):
            print("중앙선 객체를 삭제합니다.")
            self.dotLine[i].hideturtle()

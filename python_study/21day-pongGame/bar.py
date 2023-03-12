from turtle import Turtle


class Bar():

    def __init__(self, position):
        super().__init__()
        self.bar = []
        for i in range(5):
            bar_part = Turtle()
            bar_part.shape("square")
            bar_part.color("white")
            bar_part.speed("fastest")
            bar_part.penup()
            # position을 정하는 경우 중앙을 기점으로 셋팅
            if position == "right":
                bar_part.setposition(400, i*20)
            else:
                bar_part.setposition(-400, i*20)
            self.bar.append(bar_part)

    def upMove(self):
        for i in range(0, len(self.bar)):
            if self.bar[i].heading() != 90:
                self.bar[i].setheading(90)
            self.bar[i].forward(20)

    def downMove(self):
        for i in range(0, len(self.bar)):
            if self.bar[i].heading() != 270:
                self.bar[i].setheading(270)
            self.bar[i].forward(20)

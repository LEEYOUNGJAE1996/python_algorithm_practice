from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self, position1):
        super().__init__()
        self.grade = 0

        self.NewPlayerScore(position=position1)

    def NewPlayerScore(self, position):
        # 거북이는 제거
        self.hideturtle()
        self.color("white")
        # board도 새로운 turtle 객체임을 인지
        self.penup()
        if position == "left":
            self.goto(-60, 250)
        else:
            self.goto(60, 250)
        # 점수판을 보여주는 함수
        self.write(arg=f"{self.grade}",
                   align=ALIGN, font=FONT)

    # # 점수 추가
    def plusScore(self):
        self.grade += 1
        self.clear()
        self.write(arg=f"{self.grade}",
                   align=ALIGN, font=FONT)

    # # 게임이 끝난 경우

    def gameOver(self, player):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game Over\n{player} Win\nScore: {self.grade}",
                   align=ALIGN, font=FONT)

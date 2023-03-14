from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")

# Turtle의 모든 기능을 상속 받음


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.grade = 0
        with open("D:\\workstation\\python_algorithm_practice\\python_study\\19~20day-뱀게임(animation,position)\\data.txt", mode="r", encoding='UTF8') as data:
            self.high_score = int(data.read())
        # 거북이는 제거
        self.hideturtle()
        self.color("white")
        # board도 새로운 turtle 객체임을 인지
        self.penup()
        self.goto(0, 270)
        # 점수판을 보여주는 함수
        self.write(arg=f"Score: {self.grade}",
                   align=ALIGN, font=FONT)

    # 뱀이 음식을 먹은 경우
    def plusScore(self):
        self.grade += 1
        self.update_scoreboard()
    # 게임이 끝난 경우

    def gameOver(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game Over\nScore: {self.grade}",
                   align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.grade} High Score : {self.high_score}",
                   align=ALIGN, font=FONT)

    def reset(self):
        if self.high_score < self.grade:
            self.high_score = self.grade
        self.grade = 0
        self.update_scoreboard()
        self.checkScoreDB()

    def checkScoreDB(self):
        with open("D:\\workstation\\python_algorithm_practice\\python_study\\19~20day-뱀게임(animation,position)\\data.txt", mode="w") as data:
            data.write(f"{self.high_score}")

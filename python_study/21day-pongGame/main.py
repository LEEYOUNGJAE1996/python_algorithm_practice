# 230312
from turtle import Screen
from score import Score
from dotLine import DotLine
from bar import Bar
from ball import Ball
import time
# 스크린 객체를 생성
screen = Screen()
# 화면 크기 셋팅
screen.setup(width=900, height=600)
# 스크린 배경화면색 설정
screen.bgcolor("black")
# 창 타이틀 설정
screen.title("pong game")
# 스크린에서 사용자의 입력 값을 듣기 위해서
screen.listen()
# 애니메이션 기능 제거
screen.tracer(0)

score1 = Score(position1="left")
score2 = Score(position1="right")

# 중앙선 생성
middle_line = DotLine()

# 뱀 객체처럼 각각의 바를 만들기
bar1 = Bar("left")
bar2 = Bar("right")
screen.onkey(key="Up", fun=bar2.upMove)
screen.onkey(key="Down", fun=bar2.downMove)
screen.onkey(key="w", fun=bar1.upMove)
screen.onkey(key="s", fun=bar1.downMove)

# ball 객체 생성
ball = Ball()

# 게임 시작
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.upDownMoving()
    ball.checkBar(Bar=bar1.bar)
    ball.checkBar(Bar=bar2.bar)
    ball.moving()


screen.exitonclick()

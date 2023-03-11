# 230311

# 스크린을 다루기 위한 turtle 모듈을 import
from turtle import Screen
# 너무 빠른 이동을 제어
import time
from Snake import Snake
# 움직임을 지정
# 뱀의 움직임을 지정하는 객체 생성
# food import
from food import Food
# score를 다루는 객체 생성
from score import Score

# 스크린 객체를 생성
screen = Screen()
# 화면 크기 셋팅
screen.setup(width=600, height=600)
# 스크린 배경화면색 설정
screen.bgcolor("black")
screen.title("snake game")
# 스크린에서 사용자의 입력 값을 듣기 위해서
screen.listen()
# 애니메이션 기능 제거
screen.tracer(0)

# TODO : 1. 화면에 스네이크 몸 생성
# 3개의 20* 20일 지닌 각각의 객체를 생성
snake = Snake()
food = Food()
score = Score()
screen.update()
# TODO : 2. 뱀을 움직이게 만들자 객체가 전부 움직여야한다.
game_on = True
screen.onkey(key="w", fun=snake.northDirection)
screen.onkey(key="a", fun=snake.westDirection)
screen.onkey(key="s", fun=snake.southDirection)
screen.onkey(key="d", fun=snake.eastDirection)
while game_on:
    screen.update()
    time.sleep(0.1)

    # 객체 지향화
    snake.moveSnake()

    # 어떻게 뱀의 몸을 의미하는 객체와 음식을 의미하는 객체가 부딪치면 인식하고
    # 뱀의 몸의 길이는 증가하며, 음식은 다른 위치에서 생성하게 할 수 있을까?(뱀의 몸과 다른 위치에 존재)
    if snake.snake[0].distance(food) < 15:
        snake.plusBody()
        food.newFood()
        score.plusScore()
    # 벽에 충돌했는지 안했는지 판단.
    if snake.snake[0].xcor() < -300 or snake.snake[0].xcor() > 280 or snake.snake[0].ycor() < -300 or snake.snake[0].ycor() > 280:
        game_on = False
    if game_on != False:
        game_on = snake.checkBodyPosition()
    if game_on == False:
        score.gameOver()
# 클릭 할 경우 화면 탈출
screen.exitonclick()

from turtle import Turtle
# 고정값 상수화!
MOVE_DISTANS = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            snake_part = Turtle()
            snake_part.shape("square")
            snake_part.color("white")
            snake_part.width(20)
            snake_part.penup()
            snake_part.setposition((-1)*i*20, 0)
            self.snake.append(snake_part)

    def moveSnake(self):
        for i in range(len(self.snake)-1, 0, -1):
            # 앞 객체의 좌표 얻기
            new_x = self.snake[i-1].xcor()
            new_y = self.snake[i-1].ycor()
            # 객체 위치 셋팅
            self.snake[i].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANS)

# 방향 컨트롤시 반대 방향으로 갈 수 없도록 지정

    # 오른

    def eastDirection(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)

    # 위

    def northDirection(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    # 아래

    def southDirection(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    # 왼

    def westDirection(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)
    # 몸 길이 증가

    def plusBody(self):
        snake_part = Turtle()
        snake_part.shape("square")
        snake_part.color("white")
        snake_part.width(20)
        snake_part.penup()
        new_x = self.snake[-1].xcor()
        new_y = self.snake[-1].ycor()
        snake_part.setposition(new_x, new_y)
        self.snake.append(snake_part)
    # 주의할점 --- 인프리터 언어로 무조건 실행 --- return꼭 하는지 check 필요

    def checkBodyPosition(self):
        # 슬라이싱을 통해 범위 지정
        for seg in self.snake[1:]:
            if self.snake[0].distance(seg) < 10:
                return False
        return True

    def reset(self):
        for snake in self.snake:
            snake.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()

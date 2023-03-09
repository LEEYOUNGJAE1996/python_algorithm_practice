# 230309

from turtle import Turtle, Screen
import random
colors = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]
y_location = [90, 60, 30, 0, -30, -60, -90]
turtle_list = []
screen = Screen()

# 화면 셋팅
screen.setup(width=500, height=400)
# return string 형태 ---- 새로운 창을 열고 사용자로부터 입력 값을 받는다.
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ").lower()
# list 에 값 추가하기
# 어떻게 같은 이름에 객체를 여러개 생성????
# 그럼 어떻게 다룸???
for i in range(7):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    # turtle 위치 셋팅
    turtle.penup()
    turtle.goto(x=-230, y=y_location[i])
    # list를 통해 객체를 구분해준다.
    # 이름이 같더라도 다른 주소값을 저장하고 있다
    # 하지만 이것을 구분하기 위해서는 list에 따로 저장하여 같은 이름이지만
    # 다른 주소값을 가지고 있음을 구분해줘야 다른 객체로서 사용할 수 있다.
    turtle_list.append(turtle)
winner = ""
# user가 내기를 걸음?
if user_bet:
    race_on = True


while race_on:
    for race_turtle in turtle_list:
        if race_turtle.xcor() >= 230:
            winner = race_turtle.color()
            print(winner)
            race_on = False
        else:
            rand_distance = random.randint(0, 10)
            race_turtle.forward(rand_distance)

if winner == user_bet:
    print("you win")
else:
    print("you lose")


screen.exitonclick()

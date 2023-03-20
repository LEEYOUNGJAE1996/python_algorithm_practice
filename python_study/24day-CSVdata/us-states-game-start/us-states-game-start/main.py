import turtle
import pandas
screen = turtle. Screen()
screen.title("US states Game")
image = "D:\\workstation\\python_algorithm_practice\\python_study\\24day-CSVdata\\us-states-game-start\\us-states-game-start\\blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv(
    "D:\\workstation\\python_algorithm_practice\\python_study\\24day-CSVdata\\us-states-game-start\\us-states-game-start\\50_states.csv")

# 주 데이터 뽑아오기
all_states = data.state.to_list()
missing_states = []
guess_states = []
while len(guess_states) < 50:
    # 첫번째 알파벳을 대문자로 만들어주는 title() 메서드
    answer_state = screen.textinput(
        title=f"{len(guess_states)}/50 Guess the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        for state in all_states:
            if state not in guess_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(
            "D:\\workstation\\python_algorithm_practice\\python_study\\24day-CSVdata\\us-states-game-start\\us-states-game-start\\states_to_learn.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # item만을 반환하는
        t.write(state_data.state.item())
        guess_states.append(answer_state)

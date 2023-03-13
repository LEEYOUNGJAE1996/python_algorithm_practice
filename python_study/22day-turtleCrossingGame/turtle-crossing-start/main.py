import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from car_manager import CarManager
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

# 키보드 입력을 받기 위해 !!! listen() 필요
screen.listen()
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=player.forwardMove)
screen.onkey(key="Down", fun=player.backwardMove)
game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.create_cars()
    car_manager.moveCars()
    if player.smash(car_manager.all_cars) == False:
        game_is_on = False
        scoreboard.gameOver()

    if player.goal():
        car_manager.speedUp()
        scoreboard.levelUp()
    screen.update()

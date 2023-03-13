from turtle import Turtle
import random as rd
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = rd.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(rd.choice(COLORS))
            random_y = rd.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def moveCars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def speedUp(self):
        self.speed += MOVE_INCREMENT

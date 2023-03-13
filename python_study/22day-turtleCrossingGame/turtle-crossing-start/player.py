from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setposition(STARTING_POSITION)
        self.setheading(90)

    def forwardMove(self):
        self.forward(MOVE_DISTANCE)

    def backwardMove(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def smash(self, all_cars):
        for car in all_cars:
            if car.distance(self) < 20:
                return False
        return True

    def goal(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False

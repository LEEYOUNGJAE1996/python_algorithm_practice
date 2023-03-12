from turtle import Turtle


class Ball():
    updown = +10
    leftRight = +10

    def __init__(self):
        super().__init__()
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.shapesize(0.5)
        self.ball.penup()
        self.ball.speed("fastest")
        self.ball.color("purple")

    def newBall(self):
        self.ball.setposition(0, 0)

    def upDownMoving(self):
        if self.ball.ycor() > 290 and self.updown == 10:
            self.updown = -10
        elif self.ball.ycor() < -290 and self.updown == -10:
            self.updown = +10

    def moving(self):
        new_x = self.ball.xcor()+self.leftRight
        new_y = self.ball.ycor()+self.updown
        self.ball.goto(new_x, new_y)

    def checkBar(self, Bar):
        for i in range(len(Bar)):
            if self.ball.distance(Bar[i]) < 30:
                if self.leftRight == 10:
                    self.leftRight = -10
                else:
                    self.leftRight = 10

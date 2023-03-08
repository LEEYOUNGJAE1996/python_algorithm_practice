# 230308

from turtle import Turtle, Screen


# screen = Screen()
# screen.exitonclick()


timmy_turtle = Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.color("blueViolet")
for i in range(4):
    timmy_turtle.forward(100)
    timmy_turtle.right(90)

for i in range(10):
    timmy_turtle.forward(10)
    timmy_turtle.penup()
    timmy_turtle.forward(10)
    timmy_turtle.pendown()

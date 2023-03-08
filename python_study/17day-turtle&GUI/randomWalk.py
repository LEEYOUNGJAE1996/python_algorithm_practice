import color_list
from turtle import Turtle
import random as rd
timmy_turtle = Turtle()
timmy_turtle.pensize(5)
timmy_turtle.shape("turtle")
timmy_turtle.speed(10)
for i in range(100):
    timmy_turtle.color(rd.choice(color_list.color_list))
    timmy_turtle.forward(50)
    choice = rd.randrange(1, 4)
    timmy_turtle.right(choice*90)

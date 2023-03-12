from turtle import Turtle


class DotLine():
    def __init__(self):
        for i in range(-300, 500, 30):
            self.dotLine = []
            dot_part = Turtle()
            dot_part.shape("square")
            dot_part.color("white")
            dot_part.shapesize(0.5)
            dot_part.penup()
            dot_part.setposition(0, i)
            dot_part1 = Turtle()
            dot_part1.shape("square")
            dot_part1.color("white")
            dot_part1.shapesize(0.5)
            dot_part1.penup()
            dot_part1.setposition(0, i+10)
            dot_part2 = Turtle()
            dot_part2.shape("square")
            dot_part2.color("black")
            dot_part2.shapesize(0.5)
            dot_part2.penup()
            dot_part2.setposition(0, i+20)
            self.dotLine.append(dot_part)
            self.dotLine.append(dot_part1)
            self.dotLine.append(dot_part2)

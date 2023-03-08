# 230308

from turtle import Turtle, Screen


# screen = Screen()
# screen.exitonclick()
def draw_graph(angle_count, turtle, colors):
    turtle.color(colors)
    angle = 180 - (180 * (angle_count-2) / angle_count)
    for i in range(angle_count):
        turtle.forward(100)
        turtle.right(angle)


timmy_turtle = Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.color("blueViolet")

draw_graph(4, timmy_turtle, "red")
draw_graph(5, timmy_turtle, "orange")
draw_graph(6, timmy_turtle, "yellow")
draw_graph(7, timmy_turtle, "green")
draw_graph(8, timmy_turtle, "blue")
draw_graph(9, timmy_turtle, "navy")
draw_graph(10, timmy_turtle, "blueviolet")

# 230306

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("lightblue")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pockemon Name", ["r", "s", "d"])
table.add_column("TYPE", ["water", "fire", "wind"])

print(table)

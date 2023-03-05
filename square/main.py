from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")

# trinket colors (documentation): https://trinket.io/docs/colors
timmy.color("dark red")

#drawing a square
for i in range(0,4):
    timmy.forward(100)
    timmy.right(90)

screen = Screen()
screen.exitonclick()
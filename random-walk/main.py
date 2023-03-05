from turtle import Turtle, Screen
import random
timmy = Turtle()

# make timmy thicker
timmy.pensize(6)

# increase turtle speed
timmy.speed(9)

# change colors
colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta", "AliceBlue", "lightgreen" , "turquoise", "skyblue"] 

# random direction logic:
direction = [0,90,180,270]
for i in range(500):
    timmy.forward(25)
    timmy.pencolor(random.choice(colors))
    timmy.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
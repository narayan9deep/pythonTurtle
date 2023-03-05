from turtle import Turtle, Screen

timmy = Turtle()

#drawing a dashed line
for i in range(0,50):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

screen = Screen()
screen.exitonclick()
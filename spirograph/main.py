import turtle as t
import random
t.colormode(255)

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

timmy = t.Turtle()
timmy.speed("fastest")

def drawSpirograph(gap_size):
    for i in range(int(360/gap_size)):
        timmy.color(randomColor())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_size)

drawSpirograph(5)

screen = t.Screen()
screen.exitonclick()
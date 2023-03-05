from turtle import Turtle, Screen

timmy = Turtle()

#drawing a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon

for i in range(3,10):
    j=i
    while j>0:
        timmy.forward(100)
        timmy.right(180 - (((i-2)*180)/i))
        j -= 1

# for debugging:        
# timmy.forward(100)
# timmy.right(45)
# timmy.forward(100)


screen = Screen()
screen.exitonclick()
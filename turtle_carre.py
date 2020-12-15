import turtle

tortue=turtle.Turtle()

tortue.speed(0)
turtle.delay(0)

distance = 100
change = False
for i in range(4):
    tortue.forward(distance)
    tortue.right(90)


input()
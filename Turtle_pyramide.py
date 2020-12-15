import turtle

tortue=turtle.Turtle()
avance = 1

tortue.speed(0)
for i in range(900):
    tortue.forward(avance)
    tortue.right(90)
    avance += 1

input()
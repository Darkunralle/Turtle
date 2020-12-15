import turtle

tortue=turtle.Turtle()
avance = 0.0005

tortue.speed(0)
turtle.delay(0)
for i in range(12000):
    tortue.forward(avance)
    tortue.right(1)
    avance += 0.0005

input()
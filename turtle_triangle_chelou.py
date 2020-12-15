import turtle

tortue=turtle.Turtle()

tortue.speed(0)
x,y=50,50
for i in range(4):
        tortue.forward(100)
        tortue.right(90)

while 1 :  
    for m in range(100):
        tortue.forward(1)
        if tortue.xcor() > x-0.3 and tortue.xcor() < x+0.3:
            tortue.right(45)
            break

    for i in range(100):
        tortue.forward(1)
        if tortue.ycor() < y-0.3 and tortue.ycor() > y+0.3:
            tortue.right(90)
            break

    for m in range(100):
        tortue.forward(1)
        if tortue.xcor() > x-0.3 and tortue.xcor() < x+0.3:
            tortue.right(90)
            break

    for i in range(100):
        tortue.forward(1)
        if tortue.ycor() < y+0.3 and tortue.ycor() > y-0.3:
            tortue.right(90)
            break

    for m in range(100):
        tortue.forward(1)
        if tortue.xcor() > x-0.3 and tortue.xcor() < x+0.3:
            tortue.right(90)
            break

    

input()
import turtle
from random import randint

turtle_number = 20
turtles = []

for i in range(turtle_number):
    new_turtle = turtle.Turtle(shape='turtle')
    turtles.append(new_turtle)

for turtle in turtles:
    turtle.penup()
    turtle.speed(randint(0, 10))
    turtle.goto(randint(-300, 300), randint(-300, 300))
    turtle.seth(randint(0, 360)) 

while True:
    for g in range(len(turtles)):
        angle1 = turtles[g].heading()
        x1, y1 = turtles[g].pos()
        for h in range(len(turtles)):
            if g != h:
                x2, y2 = turtles[h].pos()
                angle2 = turtles[h].heading()
                dx = abs(x1-x2)
                dy = abs(y1-y2)
                if dx <= 5 and dy <=5:
                    turtles[h].seth(-angle2)
                    turtles[g].seth(-angle1)
                    turtles[h].fd(15)
                    turtles[g].fd(15)
        if x1 < -300 or x1 > 300:
            turtles[g].seth(180 - angle1)
        elif y1 < -300 or y1 > 300:
            turtles[g].seth(-angle1)
        turtles[g].fd(5)

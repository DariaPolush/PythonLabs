import turtle
t = turtle.Turtle()
t.shape("turtle")

a = 50
b = 2*a
gap = 15

t.penup()
t.backward(200)
t.left(90)
t.forward(a)
t.left(180)

def draw0():
    t.pendown()
    t.forward(b)
    t.left(90)
    t.forward(a)
    t.left(90)
    t.forward(b)
    t.left(90)
    t.forward(a)

    t.right(180)
    t.penup()
    t.forward(a + gap)
    t.right(90)

def draw1():
    t.forward(a)
    t.left(135)
    t.pendown()
    t.forward((a ** 2 + a ** 2) ** 0.5)
    t.right(135)
    t.forward(b)
    
    t.penup()
    t.left(90)
    t.forward(gap)
    t.left(90)
    t.forward(b)
    t.left(180)

def draw4():
    t.pendown()
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.left(90)
    t.penup()
    t.forward(a)
    t.pendown()
    t.left(180)
    t.forward(b)

    t.penup()
    t.left(90)
    t.forward(gap)
    t.left(90)
    t.forward(b)
    t.right(180)

def draw7():
    t.left(90)
    t.pendown()
    t.forward(a)
    t.right(135)
    t.forward((a ** 2 + a ** 2) ** 0.5)
    t.left(45)
    t.forward(a)
    t.left(90)
    
    t.penup()
    t.forward(a + gap)
    t.left(90)
    t.forward(b)
    t.left(180)


for d in [1, 4, 1, 7, 0, 0]:
    if d == 0:
        draw0()
    elif d == 1:
        draw1()
    elif d == 4:
        draw4()
    elif d == 7:
        draw7()
    

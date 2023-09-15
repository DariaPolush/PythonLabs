import turtle
t = turtle.Turtle()
t.shape("turtle")

a = 50
b = 100
c = 15
d = (a ** 2 + a ** 2) ** 0.5

#начало
t.penup()
t.backward(200)
t.left(45)

#1
t.pendown()
t.forward(d)
t.right(135)
t.forward(b)

#переход
t.penup()
t.left(90)
t.forward(c)
t.left(90)
t.forward(b)
t.left(180)

#4
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

#переход
t.penup()
t.left(90)
t.forward(c)
t.left(90)
t.forward(a)
t.right(45)

#1
t.pendown()
t.forward(d)
t.right(135)
t.forward(b)

#переход
t.penup()
t.left(90)
t.forward(c)
t.left(90)
t.forward(b)
t.right(90)

#7
t.pendown()
t.forward(a)
t.right(135)
t.forward(d)
t.left(45)
t.forward(a)
t.left(90)

#переход + 0

for i in range(2):
    t.penup()
    t.forward(a + c)
    t.left(90)
    
    t.pendown()
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.right(180)

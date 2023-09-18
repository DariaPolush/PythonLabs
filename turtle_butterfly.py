import turtle
t = turtle.Turtle()
t.shape('turtle')

n = 1
t.left(90)
for i in range(20):
    for i in range(72):
        t.forward(n)
        t.right(5)

    for i in range(72):
        t.forward(n)
        t.left(5)

    n += 1

import turtle
t = turtle.Turtle()
t.shape("turtle")
for i in range(4):
  for i in range(72):
    t.forward(5)
    t.right(5)
  for i in range(72):
    t.forward(5)
    t.left(5)
  t.left(45)

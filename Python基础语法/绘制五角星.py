from turtle import Turtle
p = Turtle()
p.speed(1)
p.pensize(5)
p.color('black','yellow')
p.begin_fill()
for i in range(5):
    p.fd(200)
    p.right(144)
p.end_fill()


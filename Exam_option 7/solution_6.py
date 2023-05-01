from turtle import *

left(90)
n = 20
right(45)
for i in range(7):
    forward(n * 6)
    right(45)
    forward(12 * n)
    right(135)
pu()
for x in range(-1, 20):
    for y in range(-1, 10):
        goto(x * n, y * n)
        dot()
done()

from turtle import *

n = 20
left(90)
right(135)
for i in range(25):
    forward(8 * n)
    right(90)
pu()
for x in range(-10, 10):
    for y in range(-20, 1):
        goto(x * n, y * n)
        dot()
done()

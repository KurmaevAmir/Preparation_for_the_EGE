from turtle import *

left(90)
n = 20
right(45)
for i in range(7):
    forward(5 * n)
    right(45)
    forward(10 * n)
    right(135)
pu()
for x in range(-1, 15):
    for y in range(-1, 7):
        goto(x * n, y * n)
        dot()
done()

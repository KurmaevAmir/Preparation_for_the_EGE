from turtle import *

left(90)
n = 10
forward(50 * n)
for i in range(4):
    right(90)
    forward(50 * n)
pu()
for x in range(-2, 52):
    for y in range(-2, 52):
        goto(x * n, y * n)
        dot()
done()
#2401

from turtle import *

left(90)
n = 20
for i in range(6):
    forward(13 * n)
    right(120)
pu()
for i in range(-1, 16):
    for j in range(-1, 16):
        goto(i * n, j * n)
        dot()
done()

from turtle import *

left(90)
n = 20
for i in range(5):
    forward(7 * n)
    right(90)
    forward(4 * n)
    right(90)
pu()
for x in range(-1, 5):
    for y in range(-1, 8):
        goto(x * n, y * n)
        dot()
done()

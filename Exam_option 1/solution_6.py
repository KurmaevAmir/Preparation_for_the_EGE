from turtle import *

left(90)
n = 20
for i in range(7):
    forward(10 * n)
    right(120)
pu()
for x in range(0, 12):
    for y in range(0, 12):
        goto(x * n, y * n)
        dot()
done()
# 38

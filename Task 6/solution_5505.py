from turtle import *

n = 20
left(90)
for i in range(8):
    forward(12 * n)
    right(90)
pu()
for x in range(-1, 14):
    for y in range(-1, 14):
        goto(x * n, y * n)
        dot()
done()
# 121

from turtle import *

left(90)
n = 20
x, y = 0, 0
for i in range(5):
    x += 6
    y += 8
    goto(x * n, y * n)
    x += -8
    y += 4
    goto(x * n, y * n)
    x += 2
    y += -12
    goto(x * n, y * n)
pu()
for i in range(-5, 10):
    for j in range(-2, 20):
        goto(i * n, j * n)
        dot()
done()
# 8

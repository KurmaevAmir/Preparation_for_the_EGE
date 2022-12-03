from turtle import *

n = 20
left(90)
x, y = 0, 0
for i in range(11):
    x += 4
    y += 4
    goto(x * n, y * n)
    x += -9
    y += 1
    goto(x * n, y * n)
    x += 5
    y += -5
    goto(x * n, y * n)
pu()
for x in range(-15, 10):
    for y in range(-1, 10):
        goto(x * n, y * n)
        dot()
done()
# 16

from turtle import *

n = 20
x, y = 0, 0
left(90)
for i in range(2):
    x += 3
    y += 4
    goto(x * n, y * n)
    x += -3
    y += 4
    goto(x * n, y * n)
    x += -3
    y += -4
    goto(x * n, y * n)
    x += 3
    y += -4
    goto(x * n, y * n)
pu()
for x in range(-7, 7):
    for y in range(-1, 9):
        goto(x * n, y * n)
        dot()
done()
# 23

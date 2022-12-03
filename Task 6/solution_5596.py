from turtle import *

n = 20
x, y = 0, 0
left(90)
for i in range(2):
    x += 6
    y += 2
    goto(x * n, y * n)
    x += 0
    y += -2
    goto(x * n, y * n)
for i in range(3):
    x += 2
    y += -1
    goto(x * n, y * n)
    x += -2
    y += -1
    goto(x * n, y * n)
for i in range(6):
    x += -2
    y += 1
    goto(x * n, y * n)
pu()
for x in range(15):
    for y in range(-8, 5):
        goto(x * n, y * n)
        dot()
done()
#54

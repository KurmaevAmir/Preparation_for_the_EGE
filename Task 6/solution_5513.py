from turtle import *

n = 20
left(90)
x, y = 0, 0
for i in range(10):
    x += -6
    y += 9
    goto(x * n, y * n)
    x += 6
    y += -2
    goto(x * n, y * n)
    x += -3
    y += -6
    goto(x * n, y * n)
pu()
for x in range(-40, 5):
    for y in range(20):
        goto(x * n, y * n)
        dot()
done()
#44

from turtle import *

n = 20
x, y = 0, 0
left(90)
for i in range(13):
    x += 4
    y += 3
    goto(x * n, y * n)
    x += -5
    y += 10
    goto(x * n, y * n)
    x += 6
    y += -6
    goto(x * n, y * n)
    x += -5
    y += -8
    goto(x * n, y * n)
done()
# 13

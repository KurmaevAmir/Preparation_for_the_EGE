from turtle import *

speed(1000)
left(90)
n = 10
x, y = 0, 0
for i in range(7):
    x += 6
    y += -9
    goto(x * n, y * n)
    x += -6
    y += 2
    goto(x * n, y * n)
    x += 12
    y += 3
    goto(x * n, y * n)
pu()
for x in range(-2, 100):
    for y in range(-35, 1):
        goto(x * n, y * n)
        dot()
done() # 50

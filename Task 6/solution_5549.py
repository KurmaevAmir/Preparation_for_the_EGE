from turtle import *

n = 20
left(90)
forward(9 * n)
right(90)
for i in range(2):
    forward(3 * n)
    right(90)
    forward(3 * n)
    right(270)
for i in range(2):
    forward(3 * n)
    right(90)
forward(9 * n)
pu()
for x in range(-1, 11):
    for y in range(-1, 11):
        goto(x * n, y * n)
        dot()
done()
# 37

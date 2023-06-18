from turtle import *

left(90)
n = 20
for i in range(2):
    forward(7 * n)
    right(90)
    forward(18 * n)
    right(90)
pu()
forward(2 * n)
right(90)
forward(9 * n)
left(90)
pd()
for i in range(2):
    forward(8 * n)
    right(90)
    forward(5 * n)
    right(90)
pu()
for x in range(8, 15):
    for y in range(-1, 9):
        goto(x * n, y * n)
        dot()
done()

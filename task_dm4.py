from drawman import *
from time import sleep
scale = 100

def f(x):
    return x**2

x = 0
y = 0
dx = 0.1
while x < 3:
    dy = f(x + dx) - y
    x = x + dx
    y = f(x)
    shift(dx*scale, dy*scale)

x = 0
y = 0
dx = -0.1
while x > -3:
    dy = f(x + dx) - y
    x = x + dx
    y = f(x)
    shift(dx*scale, dy*scale)

sleep(2)

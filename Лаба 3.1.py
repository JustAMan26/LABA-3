# -*- coding: cp1251 -*-
from math import *

print('Введите Xbeg, Xend и Dx ')
xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))

print("Xbeg={0: 7.2f} Xend={1: 7.2f}".format(xb, xe))
print("  Dx={0: 7.2f}".format(dx))

xt = xb
print("+--------+--------+")
print("|   X    |   Y    |")
print("+--------+--------+")

while xt <= xe:
    if xt <= 0:
        y = -xt / 2
    elif xt > 0 and xt <= 2:
        y = 2 - sqrt(4 - xt**2)
    elif xt > 2 and xt <= 4:
        y = sqrt(4 - (xt - 2)**2)
    else:
        y = -xt / 2 + 2

    print("|{0: 7.2f} |{1: 7.2f} |".format(xt, y))
    xt += dx

print("+--------+--------+")
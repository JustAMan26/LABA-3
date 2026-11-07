# -*- coding: cp1251 -*-
from math import *
from random import *

flag = 0
print("    X       Y      Res")
print("-------------------------")

for n in range(10):
    x = uniform(-1, 6)
    y = uniform(-4, 6)

    if (x >= abs(y)) and (y >= (x - 2)**2 - 3):
        flag = 1
    else:
        flag = 0

    print("{0: 7.2f} {1: 7.2f}  ".format(x, y), end="")
    if flag:
        print("Yes")
    else:
        print("No")
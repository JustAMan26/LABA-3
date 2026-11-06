# -*- coding: cp1251 -*-
from math import *

print('Введите Xbeg, Xend, Dx и Eps')
xb = float(input('Xbeg= '))
xe = float(input('Xend= '))
dx = float(input('Dx= '))
eps = float(input('Eps= '))

print("+--------+--------+-----+")
print("I  X I  Y I  N I")
print("+--------+--------+-----+")

xt = xb
while xt <= xe:
    # Начальные значения для ряда
    an = xt       # Первый член ряда (a_0 = x)
    n = 0         # Счётчик просуммированных членов
    s = an        # Сумма ряда (x + ...)
    
    while True:
        # Рекуррентный коэффициент
        k = ((2*n + 1)**2 * xt**2) / ((2*n + 2) * (2*n + 3))
        an = an * k
        s = s + an
        n = n + 1
        
        # Проверка достижения заданной точности
        if abs(an) < eps:
            break
    
    # Вычисление arccos(x) = pi/2 - S
    y = pi/2 - s
    
    # Вывод строки таблицы
    print("I{0: 7.2f} I{1: 7.3f} I{2: 4} I".format(xt, y, n))
    xt = xt + dx

print("+--------+--------+-----+")
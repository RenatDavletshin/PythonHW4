# Вычислить число с заданной точностью d.

import math

d = input('Введите степень округления : ')
d = d[2:len(d)]
print(round(math.pi,len(d)))
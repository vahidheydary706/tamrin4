import math
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

d = (b - (a** 2 / 3))
e = (2 * (a ** 3 / 27)) - ((a * b) / 3 + c)
f = ((e ** 2) / 4) + ((d ** 3) / 27)

if f > 0:
    g = (-e / 2 + math.sqrt(f)) ** 1 / 3 + (-e / 2 + math.sqrt(f)) ** 1 / 3 / (a / 3)
    print(g)

elif f == 0:
    h = -2 * (e / 2) ** 1 / 3 + (-e / 2 -math.sqrt(f)) **1 / 3 / (a / 3)
    i = (e / 2) ** 1 / 3 - (a / 3)
    print(h, i)

else:
    print('No answer')

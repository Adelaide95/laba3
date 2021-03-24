
import math

x1 = int(input("Введи координату X1: "))
y1 = int(input("Введи координату Y1: "))
x2 = int(input("Введи координату X2:  "))
y2 = int(input("Введи координату Y2: "))
x3 = int(input("Введи координату X3: "))
y3 = int(input("Введи координату Y3: "))
a = math.sqrt( pow(x2 - x1, 2) + pow(y2 - y1, 2) )
b = math.sqrt( pow(x3 - x2, 2) + pow(y3 - y2, 2) )
c = math.sqrt( pow(x3 - x1, 2) + pow(y3 - y1, 2) )
p = (a + b + c) / 2
S = math.sqrt( p*(p - a)*(p - b)*(p - c) )
print(S)

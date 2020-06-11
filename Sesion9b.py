from MyLibrary import *

print(seasonName(16, 1))
print(seasonName( 5, 2))
print(seasonName(12, 3))
print(seasonName(25, 3))
print(seasonName(16, 4))
print(seasonName(10, 5))
print(seasonName(19, 6))
print(seasonName(28, 6))
print(seasonName(27, 7))
print(seasonName(10, 8))
print(seasonName(19, 9))
print(seasonName(30, 9))
print(seasonName(7, 10))
print(seasonName(20, 11))
print(seasonName(19, 12))
print(seasonName(25, 12))
print(seasonName(35, 3))
print(seasonName(20, 13))

edad1 = inputData(1, 50, "Edad")
edad2 = inputData(1, 50, "Edad")
peso1 = inputData(30, 100, "Peso")
peso2 = inputData(30, 100, "Peso")
estatura1 = inputData(1.30, 1.99, "Estatura")
estatura2 = inputData(1.30, 1.99, "Estatura")

print(edad1, peso1, estatura1)
print(edad2, peso2, estatura2)

def fact(x):
    if x < 0:       # x = -1, -2, -3, ...,
        return 0
    elif x <= 1:    # x = 0, 1
        return 1
    else:           # x = 2, 3, 4, ...,
        f = 1
        for i in range(2, x + 1):
            f *= i     # f = 1 x 2 x 3 x ... X
            # f = f * i
        return f

N = int(input("Escriba el tamaño del conjunto (N):"))
M = int(input("Escriba el tamaño del subconjunto (M):"))

C = fact(N) / (fact(M) * fact(N - M))
print("Existen", int(C), "combinaciones sin repetición")

'''
C =   N!
    -------
    M!(N-M)!
'''

import MyLibrary
min = MyLibrary.Min(6.5, 10)
print(min)
max = MyLibrary.Max(6.5, 10)
print(max)
max = MyLibrary.Max(6.5, MyLibrary.Max(8.7, 7.6))
print(max)

import MyLibrary as ML
max = ML.Max(6.5, ML.Max(8.7, 9.8))
print(max)
print(ML.Min(8, 5))

from MyLibrary import Min
print(Min(8, 5))

from MyLibrary import *
print(Min(8, 5))
print(Max(8, 5))

import math
print(math.sqrt(37))

import math as M
print(M.sqrt(58))

from math import sqrt
print(sqrt(87))

from math import *
print(log(64, 2))
print(radians(90))
print(sin(0.8))



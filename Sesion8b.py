'''
myList3 = ["hola", "mundo", "feliz", "adiós", "feliz"]
i = myList3.index("feliz")
print(i)
if "contento" in myList3:
    i = myList3.index("contento")
    print(i)
'''

N = int(input("¿Cuántos nombres vas a capturar? "))
listaNombres = []
for c in range(N):    # c = 0, 1, 2, 3, ..., N - 1
    nombre = input("Nombre " + str(c + 1) + ": ").upper()
    nombre = nombre.replace("É", "E").replace("Á", "A").replace("Í", "I").replace("Ó", "O").replace("Ú", "U").replace(" ", "")
    if nombre in listaNombres:
        pos = listaNombres.index(nombre)
        listaNombres.insert(pos, nombre)
    else:
        listaNombres.append(nombre)

print(listaNombres)

myRange = range(1, 100, 6)
myList4 = list(myRange)
print(myList4)
myList5 = list(range(1, 100, 9))
print(myList5)
myList6 = list(range(50))
print(myList6)
myList7 = list(range(60, 10, -3))
print(myList7)
myList8 = list(range(8, 81, 8))
print(myList8)

# Crear una lista que tenga veinte seises
myList9 = ["seis" for c in range(20)]
print(myList9)

myList9 = []
for c in range(20):
    myList9.append("seis")
print(myList9)

myList10 = [3*(c+1) for c in range(20)]
print(myList10)

myList11 = ["Elemento " + str(c + 1) for c in range(20)]
print(myList11)

myList12 = [c for c in range(20) if c % 3 != 0]
print(myList12)
# Esquema tradicional equivalente al anterior:
myList12 = []
for c in range(20):
    if c % 3 != 0:
        myList12.append(c)
print(myList12)

# Crear la serie: [0.1, 0.2, 0.3, ... 1.0]
myList13 = [c / 10 for c in range(1, 11)]
print(myList13)

import math

# Crear la serie que tiene las raíces cuadradas de los primeros 50 números enteros positivos
myList14 = [math.sqrt(c) for c in range(1, 51)]
print(myList14)

# Crear la serie que contiene los recíprocos de todos los números enteros en el rango [-10, 10]
# excluyendo al cero.  Recíproco(x) = 1/x
myList15 = [1 / c for c in range(-10, 11) if c != 0]
print(myList15)

if 0 not in myList15:
    print("0 no está")


# Ejercicio final: calcular desviación estándar de N estaturas
N = int(input("¿Cuántas estaturas vas a capturar? "))
listaEstaturas = []
promedio = 0
for c in range(N):      # c = 0, 1, 2, 3, ..., N - 1
    estatura = float(input("Estatura " + str(c + 1) + ": "))
    promedio += estatura
    listaEstaturas.append(estatura)
promedio /= N

desvest = 0
#for c in range(N):
#    desvest += pow(listaEstaturas[c] - promedio, 2)

for estatura in listaEstaturas:                 # por cada elemento de la lista
    desvest += pow(estatura - promedio, 2)

desvest = math.sqrt(desvest / N)

print(listaEstaturas)
print(promedio)
print(desvest)

'''
    3
  6     =  6 x 6 x 6
pow(6, 3)
pow(base, exponente)
'''


# Solución sin tuplas
def printDate(day, month, year):
    print(str(day) + " de " + month + " de " + str(year))

day = 23
month = "Abril"
year = 2020
printDate(day, month, year)
printDate(8, "Septiembre", 2015)

# Solución con tuplas
def printDate(date):
    print(date[0], "de", date[1], "de", date[2])

date1 = (day, "Febrero", year)   # Esto es una TUPLA por tener PARÉNTESIS (a, b, c)
date2 = (5, month, 1989)
printDate(date1)
printDate(date2)
# printDate(27)                  # Error: un int no se puede usar con índices
# printDate(27, 2020)            # Error: la función espera un sólo argumento, no 2
# printDate(27, "Febrero", 2020) # Error: la función espera un sólo argumento, no 3
date3 = (19, "Octubre", 2015, "Miércoles")   # No hay error porque la tupla tiene al menos 3 elementos
printDate(date3)
date4 = (30, "Julio")
# printDate(date4)               # Error: la función espera una tupla con al menos 3 elementos
date5 = [8, "Mayo", 2016, 18, 39, 57]  # Esto es una LISTA por tener CORCHETES [a, b, c]
printDate(date5)                 # No hay error porque la lista tiene al menos 3 elementos
                                 # que pueden ser accedidos con corchetes: date[0]
print(type(date1), type(date2), type(date3), type(date4))
print(type(date5))

# date2[0] = 8                   # Error: una tupla no permite modificaciones en sus elementos
# date4.append(6)                # Error: a una tupla no se le pueden añadir/eliminar elementos
# date4.add(6)
date5[0] = 9
date5.append("Jueves")
print(date5)
print(date2)

dd = int(input("¿Cuál es el día?"))
mm = int(input("¿Cuál es el mes [1-12]?"))
yy = int(input("¿Cuál es el año [1-3000]?"))
date6 = (dd, mm, yy)
printDate(date6)

from Date import *

date1 = (27, 2, 2020)
date2 = nextDate(date1)
date3 = nextDate(date2)
print(date2)
print(date3)
print(type(date2))
date4 = (31, 4, 2020)
date5 = (31, 5, 2020)
print(isValidDate(date4))
print(isValidDate(date5))
print(isValidDate((28, 2, 2015)))
print(isValidDate((29, 2, 2015)))
print(isValidDate((32, 3, 2015)))
# Operaciones comunes con los demás contenedores: len, in, for/in
print(len(date4))
if 2020 in date5:
    print("date5 tiene 2020")
for e in date5:
    print(e)

print(isValidDate((28, 2)))
date6 = nextDate((31, 12, 2008))
if date6 is None:
    print("Una fecha no válida no tiene siguiente")
else:
    print(date6)

# Crear una lista de pacientes. Cada paciente tiene: Nombre, edad, peso, estatura
# Solicitar al usuario los datos de N pacientes
#  Nombre |  Edad  |  Peso |  Estatura
#  -------|--------|-------|----------
#  Juan   |  25    | 87    | 1.85
#  María  |  32    | 62    | 1.70
#  ...
N = int(input("¿Cuántos pacientes vas a capturar?"))
pacientes = []
for i in range(N):      # i = 0, 1, 2, 3, ..., N - 1
    nombre   = input("Nombre:")
    edad     = int(input("Edad:"))
    peso     = eval(input("Peso:"))
    estatura = eval(input("Estatura:"))
    paciente = (nombre, edad, peso, estatura)
    pacientes.append(paciente)
print(pacientes)    # pacientes es una lista de tuplas de 4 elementos

for paciente in pacientes:
    print("Nombre:", paciente[0])
    print("Edad:", paciente[1])
    print("Peso:", paciente[2])
    print("Estatura:", paciente[3])
    print()

p1 = pacientes[1]       # p1 es una tupla que contiene los datos del paciente con índice 1
print("Paciente 1:", p1)
print("Nombre del paciente 1:", p1[0])
print("Edad del paciente 1:",   p1[1])

print("Paciente 2:", pacientes[2])
print("Nombre del paciente 2:", pacientes[2][0])
print("Edad del paciente 2:",   pacientes[2][1])

# pacientes[2][1], elemento 2 de la LISTA, elemento 1 de la TUPLA







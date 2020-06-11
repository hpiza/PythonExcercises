def GreetWorld():
    print("Hola mundo")

print("Adiós mundo") # Esta línea queda fuera de la función, perdió la tabulación

GreetWorld()
GreetWorld()
GreetWorld()

# Python permite redefinir una función. Esto cambio afectará a las líneas de código siguientes
def GreetWorld():
    print("Hello world")

GreetWorld()
GreetWorld()

def GreetSomebody(name):
    print("Hola", name)

GreetSomebody("Juan")
GreetSomebody("María")
GreetSomebody("Mateo")
# MeetSomebody()  Se está invocando una función que aún no se define (está abajo)
# Sólamente se puede invocar a funciones que estén definidas arriba

def MeetSomebody():
    name = input("¿Cuál es tu nombre? ")
    GreetSomebody(name)

MeetSomebody()

def Max(a, b):
    if a > b:
        print(a, "es mayor")
    elif b > a:
        print(b, "es mayor")
    else:
        print("Son iguales")

Max(3, 10)
Max(3, 2)
edad1 = 20
edad2 = int(input("Edad:"))
Max(edad1, edad2)
b = 50
a = 30
Max(b, a)
x = 4.8
Max(6.5, x)
Max(6.5, a)   # a = 30
Max("abc", "def")

apellido1 = input("Apellido 1:")
apellido2 = input("Apellido 2:")  # apellido2 = "3Vázquez"
Max(apellido1, apellido2)

Max("30", "hola")
# Max(30, "hola")  Error: no se puede comparar int/float con un str

def Greet(nombre="desconocido", saludo="hola"):
    print(saludo, nombre)

Greet("Juan", "¡Quiubo!")
Greet("John", "Hi!")
Greet("Pedro", "Hola")

Greet("Simón")
Greet()
Greet("Bonjour")
Greet(saludo="Bonjour")
Greet(saludo=input("Saludo:"), nombre=input("Nombre:"))
Greet(input("Nombre:"), input("Saludo:"))

def Max(a, b):
    if a > b:
        return a
    else:
        return b

m = Max(5, 10)
print(m)

a = eval(input("Dime un número:"))      # 25
b = eval(input("Dime otro número:"))    # 40
c = eval(input("Dime ootro número:"))   # 30
d = eval(input("Dime oootro número:"))  # 47
# m = Max(a, b)
# m = Max(m, c)
# m = Max(m, d)
m = Max(Max(Max(a, b), c), d)
m = Max(Max(a, b), Max(c, d))
m = Max(a, Max(b, Max(c, d)))
print("El mayor de los tres es:", m)

m = Max("Hola", "Hello")
print(m)

print(Max(m, "Hielo"))

def Average(a, b):
    av = (a + b) / 2
    return av

ave = Average(10, 7)
# Las variables a, b, av de Average ya no existen aquí
print(ave)
# print(av) Error porque av es una variable de la función Average, no existe afuera
print(Average(10, 8.5))

def Chicharronero(a, b, c):
    raiz = (b ** 2 - 4 * a * c) ** 0.5
    xPos = (-b + raiz) / (2 * a)
    xNeg = (-b - raiz) / (2 * a)
    return xPos, xNeg

xp, xn = Chicharronero(4, 7, 1)   # xp se vincula con xPos, xn se vincula con xNeg
print(xp, xn)

x = Chicharronero(3, 8, 2)  # x es en realidad una tupla que almacena (xPos, xNeg)
print(x)
print(type(x))
print("raíz positiva:", x[0])   # x[0] accede al primer elemento de la tupla
print("raíz negativa:", x[1])   # x[1] accede al segundo elemento de la tupla













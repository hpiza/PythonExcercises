estr = "Do#exhq#hqwhqghgru/#srfdv#sdodeudv"
dstr = ""

# descencriptar la cadena de texto estr
for c in range(len(estr)):       # c     = 0, 1, 2, 3,  len = 4
    echar = estr[c]              # echar = D,  E,  F,  8
    ecode = ord(echar)           # ecode = 68, 69, 70, 56
    dcode = ecode - 3            # dcode = 65, 66, 67, 53
    dchar = chr(dcode)           # dchar = A,  B,  C,  5
    dstr += dchar                # dstr  = "A", "AB", "ABC", "ABC5"
    # dstr = dstr + dchar

print(dstr)

day = 2
month = "Abril"
year = 2020
# fecha = "2 de Abril de 2020"
fecha = str(day) + " de " + month + " de " + str(year)     # 2 --> "2",  2020 --> "2020"
print(fecha)

#char = chr(126)
#print(char)
#unicode = ord("π")
#print(unicode)

x = 4
myList1 = [15, 3, -8, x, -1]
print(myList1)
print(len(myList1))
print(type(myList1))

listaVacia = []
print(listaVacia)
print(len(listaVacia))
print(type(listaVacia))

# Añadiendo elementos al final de la lista
listaVacia.append(10)
listaVacia.append(20)
listaVacia.append(30)
print(listaVacia)

listaVacia.insert(1, 15)
print(listaVacia)
listaVacia.insert(4, 35)
print(listaVacia)
# Si la posición donde insertar es mayor al tamaño, el dato se añade al final (append)
listaVacia.insert(7, 40)
print(listaVacia)
listaVacia.insert(0, 5)     # Insertar elemento en cierta posición
print(listaVacia)
listaVacia.remove(35)       # Eliminar elemento por valor
print(listaVacia)
listaVacia.pop(2)           # Eliminar elemento por posición
print(listaVacia)

b = 30 not in listaVacia
print(b)
b = 35 not in listaVacia
print(b)

if 60 in listaVacia:
    listaVacia.remove(60)

if 60 not in listaVacia:
    listaVacia.append(60)

listaVacia.append(5)
listaVacia.insert(2, 5)
print(listaVacia)
# remove elimina la primer ocurrencia del valor
while 5 in listaVacia:
    listaVacia.remove(5)
print(listaVacia)

# Preguntar si un caracter está dentro de una cadena de texto
b = "a" in "Guadalajara"
print(b)
b = "A" in "Guadalajara"
print(b)

# Si el valor a eliminar no existe, Python arroja un error: 'x not in list'
# listaVacia.remove(60)

myList2 = [15, 3.5, "hola", True, "adiós"]
print(myList2)
print(len(myList2))
print(type(myList2))
myList2.remove("adiós")
print(myList2)

# Leyendo elementos de una lista
first  = myList2[0]
second = myList2[1]
third  = myList2[2]
print(first, second, third)

# Modificando elementos de una lista
myList2[0] = 8
myList2[1] *= 2
myList2[2] += " mundo"
myList2[3] = False
print(myList2)

myList2.append(0)
myList2.append("último")
print(myList2, len(myList2))

str = "hola"
lstr = list(str)
print(lstr)

saludos = "hola, qué tal, buenas noches"
listaSaludos = saludos.split(",")
print(listaSaludos)
print(type(listaSaludos))




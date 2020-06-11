digitos = {8, 3, 6, 6, 3}    # El segundo 6 no se agregó, el segundo 3 no se agregó
print(digitos)
print(type(digitos))
print(len(digitos))
# print(digitos[2])   Error: un conjunto no comprende de índices [2]
digitos.add(7)          # Este 7 sí se agregó
digitos.add(8)          # Este 8 no se agregó
print(digitos)
print(len(digitos))

colores = set()
for i in range(0):
    p = input("Dime un color:").lower()
    colores.add(p)
print("Colores diferentes:", colores)

letras  = {'a', 'b', 'c', 'd', 'e'}
vocales = {'a', 'e', 'i', 'o'}
# luv = letras.union(vocales)
luv = letras | vocales      #  (|) UNION
print(luv)
print(type(luv))
vul = vocales | letras
print(vul)
# liv = letras.intersection(vocales)
liv = letras & vocales      #  (&) INTERSECCIÓN DE CONJUNTOS
print(liv)
vil = vocales & letras
print(vil)
#ldv = letras.difference(vocales)
ldv = letras - vocales      # (-) DIFERENCIA DE CONJUNTOS
print(ldv)
vdl = vocales - letras
print(vdl)

N = int(input("¿Cuántos sobres compraste? "))
album = set()
repetidas = list()
for sobre in range(1, N + 1):
    print("Sobre", sobre)
    for i in range(5):
        estampa = int(input("¿Cuál número te salió? [1-400] "))
        while(estampa < 1 or estampa > 400):
            estampa = int(input("Número incorrecto. ¿Cuál número te salió? [1-400] "))
        if estampa not in album:
            album.add(estampa)
        else:
            repetidas.append(estampa)

print("Estampitas en el album:", album)
print("Repetidas:", repetidas)

miAlbum      = { 100, 200, 300, 400, 150 }
tusRepetidas = [ 56, 89, 100, 100, 150, 200, 200, 300, 350, 350 ]
temp = []
# Las estampitas nuevas las añado a 'album', las repetidas las añado a 'temp'
# while len(tusRepetidas) > 0:
while tusRepetidas:     # Mientras 'tusRepetidas' tenga elementos
    rep = tusRepetidas.pop()    # Extrae el primer elemento de la lista
    if rep not in miAlbum:
        miAlbum.add(rep)
    else:
        temp.append(rep)
# Regresar las estampitas en 'temp' a la caja de tusRepetidas
# while len(temp) > 0:
while temp:
    rep = temp.pop()
    tusRepetidas.append(rep)

'''
for rep in tusRepetidas:        # rep = 56, 89, 100, 100, ..., 400
    if rep not in miAlbum:
        miAlbum.add(rep)
'''

print("Mi álbum:", miAlbum)
print("Tus repetidas:", tusRepetidas)

tuAlbum = { 7, 12, 18, 56, 75, 89, 100, 150, 200, 225, 300, 350, 390 }

# miAlbum es subconjunto de tuAlbum, todas las que yo tengo, tú las tienes
# es decir, miAlbun no te sirve para nada
print(miAlbum.issubset(tuAlbum))    # 400 está en miAlbum, pero no está en tuAlbum
print(miAlbum <= tuAlbum)

# Mi álbum ahora tendrá también las estampitas de tu álbum que no tenía
miAlbum = miAlbum | tuAlbum
print(miAlbum)



# Diccionarios ó Mapas
# Es una colección de pares <clave, valor>

# Crear un diccionario vacío
dictionary = dict()
print(type(dictionary))
dictionary = {}         # Llaves vacías representan un Diccionario, no un Conjunto
print(type(dictionary))
# Crear un diccionario con datos precargados
dictionary = {"Uno":"One", "Dos":"Three", "Tres":"Three", "Dos":"Two"}
# Se pueden repetir valores, pero no claves. El valor de la clave repetida reemplaza al valor anterior
print(dictionary)
print(len(dictionary))
v = dictionary["Uno"]
print(v)
v = dictionary["Dos"]
print(v)
if "Cuatro" in dictionary:
    v = dictionary["Cuatro"]
    print(v)
else:
    print("Cuatro no está en el diccionario, se añadirá")
    dictionary["Cuatro"] = "Four"

for key in dictionary:
    value = dictionary[key]
    print(key, value, sep=", ")

N = int(input("¿Cuántos sobres compraste? "))
album = set()
repetidas = dict()
for sobre in range(1, N + 1):
    print("Sobre", sobre)
    for i in range(5):
        jugador = input("¿Cuál jugador te salió? ")
        if jugador not in album:
            album.add(jugador)
        else:
            if jugador in repetidas:
                repetidas[jugador] += 1
            else:
                repetidas[jugador] = 1

print("Estampitas en el album:", album)
print("Tus repetidas:", repetidas)

M = int(input("¿Cuántos jugadores tiene tu amigo en el álbum? "))
albumAmigo = set()
for i in range(1, M + 1):
    jugadorAmigo = input("Jugador " + str(i) + ": ")
    albumAmigo.add(jugadorAmigo)

jugadoresRepetidos = repetidas.keys()                   # jugadoresRepetidos es list
jugadoresRepetidos = set(jugadoresRepetidos)            # jugadoresRepetidos es set
jugadoresQueLeSirven = jugadoresRepetidos - albumAmigo  # diferencia de conjuntos

print(albumAmigo)
print(jugadoresRepetidos)
print(jugadoresQueLeSirven)



# Imprimir tablas de multiplicar del T1 al T2
T1 = 35
T2 = 48
for T in range(T1, T2 + 1):     # (T2 + 1 - T1)
    for f in range(1, 11):      #               x 10
        p = T * f
        print(T, "x", f, "=", p)
    print()

for x in range(1, 12, 2):
    for y in range(x + 1, 13, 2):
        print(x, y, sep=", ")
print()

monto = 5000  # en pesos
plazo = 10     # en años
for tasa10 in range(30, 51, 5):
    tasa = tasa10 / 10
    print("Tasa: " + str(tasa) + "%")
    m = monto * (1 +  tasa / 100)
    for a in range(plazo):
        print(" Año ", a + 1, ", monto = $", "{0:.2f}".format(m), sep="")
        m = m * (1 +  tasa / 100)

#         012345678910
cadena = "Guadalajara, Jalisco"
print(cadena)
print(cadena[12])
print(len(cadena))
primeraLetra = cadena[0]
print(primeraLetra)
print(cadena[7])
# print(cadena[11])  Error: índice 11 fuera de rango
ultimaLetra = cadena[-1]  # Indice absoluto de -1: -1 + N = 10
print(ultimaLetra)
print(cadena[-4])         # Indice abosluto de -4: -4 + N = 7

subcadena = cadena[3:12]    # [inclusivo:exclusivo]
print(subcadena)
subcadena = cadena[:11]
print(subcadena)
subcadena = cadena[13:]
print(subcadena)
subcadena = cadena[-7:]
print(subcadena)
subcadena = cadena[:-3]
print(subcadena)
subcadena = cadena[-7:-3]
print(subcadena)
subcadena = cadena[:]
print(subcadena)
print()

N = int(input("Palabras a capturar: "))
ches = 0
for i in range(N):
    palabra = input("Palabra " + str(i + 1) + ": ").lower()
    for j in range(len(palabra) - 1):
        if palabra[j] == 'c' and palabra[j + 1] == 'h':
            ches += 1

print("Se encontraron", ches, "ches")





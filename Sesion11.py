
marcadores = open("Marcadores.csv", 'r')   # r - abrir para leer (read-only)
line = marcadores.readline()            # strip() quita espacios/enter que rodean el renglón
while line != "":        # El archivo se acaba cuando readline() devuelve la cadena vacía ""
    line = line.strip()
    if line != "":
        data = line.split(',')
        print(data[1], "-", data[3])
    line = marcadores.readline()
marcadores.close()

# Otra forma de leer un archivo de texto: ciclo for
marcadores = open("Marcadores.csv", 'r')
for line in marcadores:
    line = line.strip()
    if line != "":
        data = line.split(',')
        print(data[0], "-", data[2])
marcadores.close()

import csv
gastos = open("Gastos.csv", 'r')
gastosCsv = csv.reader(gastos, delimiter=",")
for gasto in gastosCsv:
    print("Fecha:", gasto[0], "Concepto:", gasto[1], "Monto:", gasto[2])
gastos.close()
print("----")

from datetime import datetime

gastos = open("Gastos1.csv", 'r')   # Gastos1.csv incluye un encabezado: [Fecha, Concepto, Monto]
gastosCsv = csv.DictReader(gastos)
listaFechas = list()
listaConceptos = list()
listaMontos = list()
for gasto in gastosCsv:
    fecha    = datetime.strptime(gasto['Fecha'], "%d/%m/%Y")
    concepto = gasto['Concepto']
    monto    = eval(gasto['Monto'].replace('$', '').replace(',', ''))  # '$1,536.25' --> 1536.25
    listaFechas.append(fecha)
    listaConceptos.append(concepto)
    listaMontos.append(monto)
gastos.close()

listaFechas.sort()
listaConceptos.sort()
listaMontos.sort()
print(listaFechas)
print(listaConceptos)
print(listaMontos)
primerFecha    = min(listaFechas)
ultimoConcepto = max(listaConceptos)
montoMaximo    = max(listaMontos)
print(primerFecha, ultimoConcepto, montoMaximo)

# Almacenar los gastos en una lista de tuplas
gastos = open("Gastos1.csv", 'r')
gastosCsv = csv.DictReader(gastos)
listaGastos = list()
for gasto in gastosCsv:
    fecha    = datetime.strptime(gasto['Fecha'], "%d/%m/%Y")
    concepto = gasto['Concepto']
    monto    = eval(gasto['Monto'].replace('$', '').replace(',', ''))  # '$1,536.25' --> 1536.25
    gasto = (fecha, concepto, monto)
    listaGastos.append(gasto)
gastos.close()

listaGastos.sort()     # Ordenamiento con criterios default: por Fecha, luego concepto, luego monto
for gasto in listaGastos:
    print(gasto)
print("----")

def porConcepto(gasto):
    return gasto[1]

def monto(gasto):
    return gasto[2]

def fechaConcepto(gasto):
    return gasto[0], gasto[1]

listaGastos.sort(key=fechaConcepto)
for gasto in listaGastos:
    print(gasto)
print("----")

listaGastos.sort(key=porConcepto)
for gasto in listaGastos:
    print(gasto)
print("----")
listaGastos.sort(key=monto, reverse=True)   # Ordenar de mayor a menor
for gasto in listaGastos:
    print(gasto)

import locale
 # Establece el 'locale' de nuestra región a todos los conceptos: fecha, hora, moneda, ...
locale.setlocale(locale.LC_ALL, '')

gastosPorMonto = open("GastosPorMonto.csv", "w")
for gasto in listaGastos:
    fecha = gasto[0].strftime("%d de %B de %Y")
    concepto = gasto[1]
    #monto = "$" + str(gasto[2])
    monto = locale.currency(gasto[2], grouping=True)
    gastosPorMonto.write(fecha + "," + concepto + "," + monto + "\n")
gastosPorMonto.close();

# 4-sep-2018 : { 1365.37, 675.20 } --> 2040.57
# 7-sep-2018 : {  847.56, 542.00, 187.00 } --> 1558.56
# { 4-sep-2018 : 2040.57, 7-sep-2018 : 1558.56 }
listaGastos.sort(key = fechaConcepto)
montoPorFecha = dict()
for gasto in listaGastos:
    fecha = gasto[0]
    monto = gasto[2]
    if fecha not in montoPorFecha:
        montoPorFecha[fecha] = monto
    else:
        montoPorFecha[fecha] += monto

archivoGastadoPorDia = open("GastadoPorDia.csv", "w")
for fecha in montoPorFecha:
    fechaLarga = fecha.strftime("%d/%m/%y")
    monto = montoPorFecha[fecha]
    montoFormateado = locale.currency(monto, grouping=True)
    archivoGastadoPorDia.write(fechaLarga + "," + montoFormateado + "\n")
archivoGastadoPorDia.close()
print()
listaGastos.sort(key=porConcepto)
montoPorConcepto = dict()
for gasto in listaGastos:
    print(gasto)
    concepto = gasto[1]
    monto = gasto[2]
    if concepto not in montoPorConcepto:
        montoPorConcepto[concepto] = monto
    else:
        montoPorConcepto[concepto] += monto

archivoGastadoPorConcepto = open("GastadoPorConcepto.csv", "w")
for concepto in montoPorConcepto:
    monto = montoPorConcepto[concepto]
    montoFormateado = locale.currency(monto, grouping=True)
    archivoGastadoPorConcepto.write(concepto + "," + montoFormateado + "\n")
archivoGastadoPorConcepto.close()

'''
# Manipulación de fechas con Python
d1 = datetime(2020, 4, 25)  # 25-abril-2020
print(d1)
print(type(d1))
d2 = datetime.today()
print(d2)
fecha = "28-04-2020"
d3 = datetime.strptime(fecha, "%d-%m-%Y")
print(d3)
fecha = "Feb. 27th, 2017"
d3 = datetime.strptime(fecha, "%b. %dth, %Y")
print(d3)
'''

'''
primerRenglon = marcadores.readline()
print(primerRenglon, end="")
segundoRenglon = marcadores.readline()
print(segundoRenglon, end="")
print(marcadores.readline(), end="") # tercer renglón 
print(marcadores.readline(), end="") # cuarto renglón
print(marcadores.readline(), end="")
print(marcadores.readline(), end="")
print(marcadores.readline(), end="")
print(marcadores.readline())
print("-----")
'''

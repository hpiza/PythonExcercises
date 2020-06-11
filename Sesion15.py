# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 18:02:17 2020

@author: hpiza
"""

from pandas import DataFrame
import pandas
import numpy

covidData = {  "Country" : ["USA",  "Brazil", "Russia"], 
               "Cases"   : [1870238, 539045,  423741],
               "Deaths"  : [ 107620,  30486,    5037]
}
covidIndex = [1, 2, '3']
covidDF = DataFrame(covidData, covidIndex)
print(covidDF)

autosData = { "Marca"  : ["Nissan",    "Dodge",   "Ford",   "Seat", "Nissan",   "Dodge"],
              "Modelo" : [ "March", "Attitude", "Fiesta", " Ibiza",  "Versa", "Journey"],
              "Año"    : [   2018,        2018,     2017,     2018,     2019,      2017],
              "Precio" : [ 155900,      165000,   165000,   219000,   220000,    285000]
}
autosIndex = ["Auto1", "Auto2", "Auto3", "Auto4", "Auto5", "Auto6"]
autosDF = DataFrame(autosData, autosIndex)
print(autosDF)

print(covidDF.columns.values)  # Lista con los nombres de las columnas
print(covidDF.index.values)    # Lista con los nombres de las filas
print(covidDF.values)          # Lista de listas que contiene todos los datos

# Cambiar el nombre a cada fila (índices)
covidDF.index.values[0] = "#1"
covidDF.index.values[1] = "#2"
covidDF.index.values[2] = "#3"
print(covidDF)

# Cambiar el nombre a una columna
renameColumns = { "Country" : "País", "Cases" : "Casos", "Deaths" : "Muertos"}
# inplace=True realiza los cambios sobre el mismo dataframe
covidDF.rename(columns=renameColumns, inplace=True)
print(covidDF)
# por default, inplace=False, realiza los cambios en un nuevo dataframe que se tiene que recibir
# covidDF = covidDF.rename(columns=renameColumns)

# Acceder a una celda (lectura, escritura)
# Obtener el número de casos en USA
casosUSA = covidDF.loc["#1", "Casos"]
print(casosUSA)
# Incrementar el número de muertos en Rusia
# loc permite acceder a una celda utilizando nombres de fila y columna, en lugar de índices
covidDF.loc["#3", "Muertos"] += 50
print(covidDF)
# Imprimir el número de filas y columnas de covidDF
rows = len(covidDF.index)
cols = len(covidDF.columns)
print(rows, cols)

# Ejercicio 1: sumar IVA a los precios de los autos y convertir la marca a mayúsculas
for r in range(len(autosDF.index)):
    # iloc permite acceder a una celda utilizando índices de fila y columna, en lugar de nombres
    autosDF.iloc[r, 3] *= 1.16
    autosDF.iloc[r, 0] = autosDF.iloc[r, 0].upper()
print(autosDF)
print("----------------")
covidmexDF = pandas.read_csv("Covidmex.csv", encoding="latin1", index_col=0)
print(covidmexDF)
print(covidmexDF.columns.values)
print(covidmexDF.index.values)
print(covidmexDF.loc["18-may-20"]["NuevosMue"])

# Instalar paquete 'xlrd' para leer un archivo de Excel
covidMundoDF = pandas.read_excel("Covidmundo.xlsx", index_col=0)
print(covidMundoDF)
print("----------------")
excelFile = pandas.ExcelFile("Covidmundo.xlsx")
covidWorldDF = pandas.read_excel(excelFile, "World")
covidUsaDF = pandas.read_excel(excelFile, "USA")
print(covidWorldDF)
print("----------------")
print(covidUsaDF)
print("----------------")

# Seleccionar un subconjunto de columnas: corte vertical
#   Seleccionar por nombre de columnas, mediante lista
columnas = ["Modelo", "Precio"]
autos1DF = autosDF[columnas]
print(autos1DF)
print("----------------")
#   Seleccionar por índice de columnas, mediante rangos
columnas = autosDF.columns[:2]  # Selecciona las primeras dos columnas
autos2DF = autosDF[columnas]
print(autos2DF)
print("----------------")

# Ordenar las filas por algún criterio (columnas y orden)
ordenarPor = ["Marca", "Modelo"]
ascendente = [ True,    True]
autosDF.sort_values(by=ordenarPor, ascending=ascendente, inplace=True)
print(autosDF)
print("----------------")

# Ordenar la tabla autosDF por precio: de mayor a menor.
# En caso de empate, ordenar por año, de menor a mayor
ordenarPor = ["Precio", "Año" ]
ascendente = [ False,    True ]
autosDF.sort_values(by=ordenarPor, ascending=ascendente, inplace=True)
print(autosDF)
print("----------------")

# Extraer las primeras 5 columnas de la tabla covidMundoDF y
# ordenar su filas por número de muertos de mayor a menor. Hacerlo en una línea de código
ordenarPor = ["Total deaths"]
ascendente = [ False]
#columnas   = covidMundoDF.columns[:5]
columnas   = ["Country", "Total deaths"]
covidMundoDF1 = covidMundoDF[columnas].sort_values(by=ordenarPor, ascending=ascendente)
print(covidMundoDF1)
print("----------------")

# Seleccionar de la fila 3 (cuarta fila) en adelante
filas = autosDF.index[3:]
autos3DF = autosDF.loc[filas]
print(autos3DF)
print("----------------")

# Seleccionar las filas indicadas en la lista, por su nombre
filas = ["Auto4", "Auto2", "Auto5"]
autos4DF = autosDF.loc[filas]
print(autos4DF)
print("----------------")

# Combinar la selección de filas y columnas
filas = ["Auto1", "Auto3", "Auto6"]
columnas = ["Marca", "Modelo"]
autos5DF = autosDF.loc[filas, columnas]
print(autos5DF)
print("----------------")

# Seleccionar un rango de columnas definido por el nombre de la primera y la última
autos6DF = autosDF.loc[filas, "Modelo":"Precio"]
print(autos6DF)
print("----------------")

# Seleccionar filas que cumplan alguna condición, en alguna(s) columna(s)
columnas = ["Marca", "Modelo", "Precio"]
autosBaratosDF = autosDF.loc[autosDF['Precio'] < 200000, columnas]
print(autosBaratosDF)
print("----------------")

# Seleccionar filas que en cierta columna tengo un valor en un conjunto
marcas = ("NISSAN", "SEAT")
carritosDF = autosDF.loc[autosDF["Marca"].isin(marcas)]
print(carritosDF)
print("----------------")

# Ejercicio: de covidmex, seleccionar todas las fechas cuyo número de nuevos muertos
# sea superior a 300. Incluir en el resultado: número de nuevos muertos y de nuevos casos.
# Ordenar el resultado por nuevos muertos de mayor a menor
columnas = ["NuevosMue", "NuevosPos"]
ordenarPor = ["NuevosMue"]
ascendente = [ False]
muchosMuertosDF = covidmexDF.loc[covidmexDF["NuevosMue"] > 300, columnas].sort_values(by=ordenarPor, ascending=ascendente)
print(muchosMuertosDF)
print("----------------")

# Reemplazos generalizados
#autosDF.replace(to_replace="NISSAN", value="Nissan", inplace=True)
autosDF.replace(to_replace=("NISSAN", "DODGE"), value=("Nissan", "Dodge"), inplace=True)
print(autosDF)
print("----------------")
replacements = { "SEAT":"Seat", "FORD":"Ford" }

autosDF.replace(replacements, inplace=True)
print(autosDF)
print("----------------")
# Para reemplazar sólo en una columna
autosDF["Modelo"].replace(to_replace=("Journey", "Versa"), value=("JOURNEY", "VERSA"), inplace=True)
print(autosDF)
print("----------------")

# Lidiando con valores nulos (missing values)
print(covidMundoDF[["Country", "New deaths"]])
print("----------------")
# float("NaN")
covidMundoDF["New deaths"].replace(to_replace=numpy.NaN, value=0, inplace=True)
print(covidMundoDF[["Country", "New deaths"]])

# Selecciona todas las filas de covidMundoDF que no tengan valor nulo en la columna "New cases"
# PENDIENTE, no está haciendo la selección correctamente con numpy.NaN
covidMundoDF2 = covidMundoDF.loc[covidMundoDF["New deaths"] != numpy.NaN]
print(covidMundoDF2[["Country", "New cases"]])
print("----------------")

columnas = ["Marca"]
#porMarcaDF = autosDF.groupby(columnas).count()
porMarcaDF = autosDF.groupby(columnas).mean()
print(porMarcaDF)
print("----------------")
operations = {"Año":"min", "Precio": "mean"}
porMarcaDF = autosDF.groupby(columnas).agg(operations)
print(porMarcaDF)

from matplotlib import pyplot
porMarcaDF.plot(kind="bar", y="Precio", color="blue")
pyplot.show()

axis = pyplot.gca()
covidmexDF.plot(kind="line", y="Positivos", color="#AA8844", ax=axis)
covidmexDF.plot(kind="line", y="Muertos", color="red", ax=axis)
pyplot.show()

columnas=["Continent"]
operations = {"Total cases":"sum", "Total deaths": "sum", "Total tests": "mean"}
covidContinenteDF = covidMundoDF.groupby(columnas).agg(operations)
print(covidContinenteDF)
axis = pyplot.gca()
covidContinenteDF.plot(kind="bar",  y="Total cases",  color="#66AACC", ax=axis)
covidContinenteDF.plot(kind="line", y="Total deaths", color="#66DDAA", ax=axis)
covidContinenteDF.plot(kind="line", y="Total tests",  color="#DD7799", ax=axis)
pyplot.show()



































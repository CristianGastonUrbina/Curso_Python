
"""
def costeCamion(nombreArchivo):
	suma = 0
	with open (nombreArchivo,"rt") as f:
		header = next(f)
		for file in f:
			try:
				linea = file.split(",")
				suma=suma + int(linea[1])* float(linea[2])
			except ValueError:
				print("Error en el archivo, la fruta",linea[0],"esta incompleta y se saco del calculo")
	return suma
"""
#%%
"""
import csv
def leer_camion(nombre_archivo):
	camion = []
	with open (nombre_archivo,"rt") as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			fruta = row[0]
			ncajones = int(row[1])
			precio = float(row[2])
			linea = (fruta,ncajones,precio)
			camion.append(linea)
	return camion

camion = leer_camion("C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/camion.csv")
print(camion)
"""
#%%

import csv
def leer_camion(nombre_archivo):
    """abre un archivo con el contenido de un camión, lo lee y devuelve 
        la información como una lista de diccionarios."""
    camion = []
    with open (nombre_archivo,"rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for n_row,row in enumerate(rows):
            try:
                dic_temporal = dict(zip(headers,row))
                dic_temporal["cajones"] = int(dic_temporal["cajones"])
                dic_temporal["precio"] = float(dic_temporal["precio"])
                camion.append(dic_temporal)
            except ValueError:
                print(f' Fila {n_row}: No pude interpretar: {row}')
        return camion
from pprint import pprint
camion = leer_camion("C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/camion.csv")


#%%
"""Escribí una función leer_precios(nombre_archivo) que a
 partir de un conjunto de precios como éste arme un diccionario
 donde las claves sean los nombres de frutas y verduras, y 
 los valores sean los precios por cajón."""
 
import csv
def leer_precios(nombre_archivo):
    "A partir de un archivo de precios arma un diccionario con el mismo"
    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    precios = {}
    for row in rows:
        try:
            precios[row[0]] = float(row[1])
        except IndexError:
            #Va a estar comentada para que no aparesca en la tabla
            #print("error en linea. Contenido de linea:",row,"\n\n\n" )
            pass
    return precios

#%%

"Precio de compra: camiones.csv"
"Precio de venta : precios.csv"
"Calcular lo que costo el camion"
"Calcular ganancia de venta y diferencia"

compra = leer_camion("C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/fecha_camion.csv")
venta = leer_precios("C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/precios.csv")

costoCamion = 0
for row in compra:
    costoCamion += row["cajones"]*row["precio"]

gananciaCamion = 0
for row in compra:
    gananciaCamion += row["cajones"]*venta[row["nombre"]]

balance = gananciaCamion - costoCamion

print(f"Se gasto {costoCamion} se gano {gananciaCamion} y el balance es de {balance:.2f}")
#%%
"""3.13 
Escribí una función hacer_informe() que recibe una lista de cajones y un diccionario con
 precios como input y devuelve una lista de tuplas conteniendo la información mostrada
 en la tabla anterior.

"""
def hacer_informe(camion,precios,headers):
    #Camion es una lista de diccionarios
    #Precio es un diccionario
    informe = []
    cabecera = ""
    for i in headers:
        cabecera +=f"{i:>10s} "  
    print (cabecera)
    i="-"
    print ((f"{i*10:>10} ")*4)
    for i in camion:
        fruta = i["nombre"]
        cajon = i["cajones"]
        precio_Comp = i["precio"]
        precio_Dif = precios[fruta] - precio_Comp
        tupla = (fruta,cajon,precio_Comp,precio_Dif)
        informe.append(tupla)
        print(f"{fruta:>10s} {cajon:>10d} {'$'+(str(precio_Comp)):>10s} {precio_Dif:>10.2f}")
    
    return informe

            
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')    
camion = leer_camion('../Data/fecha_camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios,headers)











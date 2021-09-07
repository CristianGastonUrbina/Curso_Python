#coste_camion.py
#Abra el archivo, lea las líneas, y calcule el precio pagado por los cajones cargados en el camión.
"""
costeCamion = 0
with open("C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/camion.csv","rt") as f:
	header = next(f)
	for file in f:
		linea = file.split(",")
		costeCamion = costeCamion + int(linea[1])*float(linea[2])

print ("El costo total es de: ",costeCamion)	
"""


"""
def costeCamion(nombreArchivo):
	suma = 0
	with open (nombreArchivo,"rt") as f:
		header = next(f)
		for file in f:
			linea = file.split(",")
			suma=suma + int(linea[1])* float(linea[2])
	return suma

costo = costeCamion("C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/camion.csv")
print(costo)
"""

##Costecamion con manejo de errores
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

costo = costeCamion("C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/camion.csv")
print(costo)
costo = costeCamion("C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/missing.csv")
print(costo)

#%%
"""costoCamion con errores usando enumerate"""
def costeCamion(nombreArchivo):
	suma = 0
	with open (nombreArchivo,"rt") as f:
		header = next(f)
		for n_fila, fila in enumerate(f):
			try:
				linea = fila.split(",")
				suma=suma + int(linea[1])* float(linea[2])
			except ValueError:
				print(f' Fila {n_fila}: No pude interpretar: {fila}')
	return suma

costo = costeCamion("C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/camion.csv")
print(costo)
costo = costeCamion("C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/missing.csv")
print(costo)
#%%
"""CostoCamion pero sin necesidad de estar en orden las columnas"""

import csv
def costeCamion(nombreArchivo):
    suma = 0
    with open (nombreArchivo,"rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for n_fila, fila in enumerate(rows):
                camion = dict(zip(header,fila))
                try:
                    ncajones= int(camion["cajones"])
                    precio = float(camion["precio"])
                    suma += ncajones*precio
                except ValueError:
                    print(f' Fila {n_fila}: No pude interpretar: {fila}')
    return suma


costo = costeCamion("C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/camion.csv")
print(costo)
costo = costeCamion("C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/missing.csv")
print(costo)
costo = costeCamion("C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/fecha_camion.csv")
print(costo)


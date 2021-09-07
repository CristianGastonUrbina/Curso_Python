 camion_commandline.py
import csv
import sys

def costo_camion(nombre_archivo):
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
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = "C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/camion.csv"

costo = costo_camion(nombre_archivo)
print('Costo total:', costo) 
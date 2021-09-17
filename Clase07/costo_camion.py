#coste_camion.py

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


#%%

#Las secciones anteriores pertenecen a versiones de otras clases del programa
"""CostoCamion pero sin necesidad de estar en orden las columnas"""
def f_principal(nombreArchivo):
    import informe_final
    camion = informe_final.leer_camion(nombreArchivo[1])
    suma = [elemento["cajones"]*elemento["precio"] for elemento in camion]
    print (sum(suma))

#%%

if __name__ == "__main__":
    import sys
    f_principal(sys.argv)
    
    
    
    
    
    
    

"""
with open("C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/precios.csv","rt") as f:
	for file in f:
			fruta = file.split(",")
			if fruta[0] == "Naranja":
				print ("El precio de la Naranja es de: ", fruta[1])
"""


##Buscar precio como se pidio

def buscar_precio(fruta):
	encontrado = False
	with open("C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/precios.csv","rt") as f:
		for file in f:
			frutaActual = file.split(",")
			if frutaActual[0] == fruta:
				print ("El precio de",fruta,"es de",frutaActual[1])
				encontrado = True
	if encontrado == False:
		print ("No se encontro a ", fruta, "en el listado")
		
buscar_precio('Frambuesa')
buscar_precio('Kale')



##Buscar precio en cualquier archivo
"""
def buscar_precio(archivo,fruta):
	encontrado = False
	with open(archivo,"rt"):
		for file in f:
			frutaActual = file.split(",")
			if frutaActual[0] == fruta:
				print ("El precio de",fruta,"es de",fruta[1])
				encontrado = True
	if encontrado = False:
		print ("No se encontro a ", fruta, "en el archivo")
"""
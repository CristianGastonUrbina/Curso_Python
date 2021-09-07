# rebotes.py
# Archivo de ejemplo
# Ejercicio
alturaInicial = 100
reduccion = 3/5
repeticiones = 10
alturaActual = alturaInicial

while repeticiones > 0:
	repeticiones -= 1
	alturaActual = alturaActual*reduccion
	print (alturaActual)
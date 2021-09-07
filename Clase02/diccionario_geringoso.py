#2.14
"""Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso.
 Las claves del diccionario deben ser las palabras de la lista y los valores deben ser sus traducciones al geringoso 
 (como en el Ejercicio 1.18). Probá tu función para la lista ['banana', 'manzana', 'mandarina']. 
 Guardá este ejercicio en un archivo diccionario_geringoso.py para entregar al final de la clase."""
 
def geringoso (palabra):
	palabrapa = ""
	for c in palabra:
		palabrapa = palabrapa + c
		if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
			palabrapa = palabrapa + "p" + c
	return palabrapa
	
def geringosLista(lista):
	dic = {}
	for i in lista:
		dic[i]= geringoso(i)
	return dic
	
print(geringosLista(['banana', 'manzana', 'mandarina']))

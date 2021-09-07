#Separador primera edicion.py
"""
palabra = "estupefaciente"
vocales = ["a","e","i","o","u"]
palabraEnSilabas=[]
silaba = ""
for i in range(len(palabra)):
	silaba = silaba + palabra[i]
	if palabra[i] in vocales:
		palabraEnSilabas.append(silaba)
		silaba = ""

print (palabraEnSilabas)
"""

"""Separador segunda edicion
	Ahora se agrega la regla que dice:
	Toda consonante que esté ubicada al final de la palabra formará sílaba con la vocal anterior.
	Por ejemplo: ca-sas, sa-ber, ár-bol.
"""
palabra = "ciudad"
vocales = ["a","e","i","o","u"]
palabraEnSilabas=[]
silaba = ""
for i in range(len(palabra)):
	silaba = silaba + palabra[i]
	print(silaba)
	if palabra[i] in vocales:
	#Es Vocal
		if i == len(palabra)-2:
		#Es la Antultima
			if palabra[i+1] not in vocales:
				silaba = silaba + palabra[i+1]
				palabraEnSilabas.append(silaba)
				break
		palabraEnSilabas.append(silaba)
		silaba = ""
print (palabraEnSilabas)

"""Separador tercera edicion
	Ahora toma en cuenta los diptongos
	"""
	palabra = "ciudad"
vocales = ["a","e","i","o","u"]
palabraEnSilabas=[]
silaba = ""
for i in range(len(palabra)):
	silaba = silaba + palabra[i]
	print(silaba)
	if palabra[i] in vocales:
	#Es Vocal
		if i == len(palabra)-2:
		#Es la Antultima
			if palabra[i+1] not in vocales:
				silaba = silaba + palabra[i+1]
				palabraEnSilabas.append(silaba)
				break
		palabraEnSilabas.append(silaba)
		silaba = ""
print (palabraEnSilabas)
	
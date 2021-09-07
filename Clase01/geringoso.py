#geringoso.py
"""
cadena = "Que"
capadepenapa = ""
for c in cadena:
	capadepenapa = capadepenapa + c
	if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
		capadepenapa = capadepenapa + "p" + c
print (capadepenapa)
"""


#geringoso.py con diptongos

cadena = "opioide"
capadepenapa = ""
for c in range(len(cadena)):
	capadepenapa = capadepenapa + cadena[c]
	#print(capadepenapa)
	#Tengo vocal?
	if  cadena[c] == "a" or cadena[c] == "e" or cadena[c] == "i" or cadena[c] == "o" or cadena[c] == "u":
		#es la ultima vocal de mi palabra?
		#print("tengo Vocal")
		if c == len(cadena) -1:
			capadepenapa = capadepenapa + "p" + cadena[c]
			break
			#Tengo Diptongo ?
		if not((cadena[c] == "i" or cadena[c] == "u") and (cadena[c+1] == "i" or cadena[c+1] == "u")) or ((cadena[c] == "a" or cadena[c] == "e" or cadena[c]== "o") and (cadena[c+1] == "i" or cadena[c+1] == "u")) or ((cadena[c+1] == "a" or cadena[c+1] == "e" or cadena[c+1] == "o") and (cadena[c] == "i" or cadena[c] == "u")): 
			#print ("tengo Diptongo y hasta ahora tengo " + capadepenapa)
			pass
		else:
			capadepenapa = capadepenapa + "p" + cadena[c]
print (capadepenapa)
		
		

#inclusive.py
frase = "Todos, tu también"
palabras = frase.split()
fraseInc = []
for palabra in palabras:
	if len(palabra) >=2:
		if palabra[-2] == "o":
			palabraInc = palabra[:-2] + "e" + palabra[-1]
		else:
			palabraInc = palabra
		fraseInc.append(palabraInc)
print(" ".join(fraseInc))
		
		
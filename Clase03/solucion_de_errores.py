# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 11:15:22 2021

@author: Cristian
"""


#Comentario: El error era de tipo semantico y estaba ubicado en el while.
#    Lo corregí sacando el return False del ciclo while.
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<=n:
        if expresion[i] == 'a' or expresion[i]== "A":
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de sintactico y estaba ubicado en en todas las lineas
#que requerian un : al final y no lo tenian, ademas expresion[i] == 'a': solo
#tenia un =. Adicionalmente return Falso esta mal deberia ser False y
#falta la condicion de a Mayuscula
# faltaba el : al def

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i]== "A":
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
#%%
#Ejercicio 3.3. Función tiene_uno()
#Errores:
"""
1984 deberia llamarse con comillas o bien atrapar el error y 
exolicar que se debe poner strings y no numeros como valor de la funcion
"""

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno("1984")
#%%
"""
Ejercicio 3.4: Alcances
Falta el return c
"""
def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
#%%
"""
Ejercicio 3.5: Pisando memoria
Se estaba pisando cada vez el mismo espacio de memoria.
Se debe vaciar o armar un diccionario diferente para que no se pise
"""
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/camion.csv')
pprint(camion)
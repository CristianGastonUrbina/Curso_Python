# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 20:57:42 2021

@author: Cristian
"""

import csv
archivo = "C:/Users/Cristian/Desktop/ejercicios_python_UNSAM/Data/arbolado-en-espacios-verdes.csv"


def leer_archivo(archivo):
    """Devuelve una lista de diccionarios con la informacion del
    archivo"""
    with open (archivo,"rt",encoding='utf8') as f:
        rows = csv.reader(f)
        header = next(rows)
        resultado = []
        for row in rows:
            dic = dict(zip(header,row))
            resultado.append(dic)
        return resultado
    
#%%

def leer_parque(archivo,parque,todos=False):
    """ abra el archivo indicado y devuelva una 
    lista de diccionarios con la información del parque especificado. La función debe devolver
    , en una lista un diccionario con todos los datos por cada árbol del parque elegido 
    (recordá que cada fila del csv es un árbol)."""
    data =leer_archivo(archivo)
    resultado = []
    for i in data:
        if todos:
            i["altura_tot"]=float(i["altura_tot"])
            i["inclinacio"]=int(i["inclinacio"])
            resultado.append(i)
        else:
            if i["espacio_ve"] == parque:
                i["altura_tot"]=float(i["altura_tot"])
                i["inclinacio"]=int(i["inclinacio"])
            resultado.append(i)
    return resultado
a = leer_parque(archivo,"GENERAL PAZ")
#%%
def especies(lista_arboles):
    """Escribí una función especies(lista_arboles) que tome una lista de árboles 
    y devuelva el conjunto de especies (la columna
    'nombre_com' del archivo) que figuran en la lista."""
    especies = []
    for row in lista_arboles:
        especies.append(row["nombre_com"])
    unicos = set(especies)
    return unicos
    
#a = leer_parque(archivo,"GENERAL PAZ")
#b = especies(a)    
    
#%%
def contar_ejemplares(lista_arboles):
    """Usando contadores como en el Ejercicio 3.11, escribí una función
    contar_ejemplares(lista_arboles) que, dada una lista como la que generada con
    leer_parque(), devuelva un diccionario en el que las especies (recordá, es la columna 
    'nombre_com' del archivo) sean las claves y tengan como valores asociados la cantidad 
    de ejemplares en esa especie en la lista dada."""
    from collections import Counter
    resultado = Counter()
    for row in lista_arboles:
        resultado[row["nombre_com"]] += 1
    return resultado

a = leer_parque(archivo,"GENERAL PAZ")
b= contar_ejemplares(a)
    
def especies_mas_comunes(archivo,parque,cant_especies):
    lista = leer_parque(archivo, parque)
    especies = contar_ejemplares(lista)
    lista_imprimir = especies.most_common(cant_especies)
    print(f"{parque:^25s}")
    print(f"{'-'*25:>25s}")
    for i in lista_imprimir:
        print(f"{i[0]:<20s}: {i[1]:<10d}")

    
especies_mas_comunes(archivo,'CENTENARIO',5)

#%%

def obtener_alturas(lista_arboles,especie):
    """Escribí una función obtener_alturas(lista_arboles, especie) que, 
    dada una lista de árboles como la anterior y una especie de árbol
    (un valor de la columna 'nombre_com' del archivo), devuelva una lista
    con las alturas (columna 'altura_tot') de los ejemplares de esa especie en la lista."""
    alturas = []
    import numpy as np
    for arbol in lista_arboles:
        if arbol["nombre_com"] == especie:
            alturas.append(arbol["altura_tot"])
    altura_max= max(alturas)
    altura_prom = np.mean(alturas)
    print(f"altura maxima de {especie}:{altura_max}")
    print(f"altura promedio de {especie}:{altura_prom}")
    return alturas

obtener_alturas(a,"Jacarandá")

#%%
def obtener_inclinaciones(lista_arboles,especie):
    """Escribí una función obtener_inclinaciones(lista_arboles, especie) que,
    dada una especie de árbol y una lista de árboles como la anterior, devuelva
    una lista con las inclinaciones (columna 'inclinacio') de los ejemplares de esa especie."""
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol["nombre_com"] == especie:
            inclinaciones.append(arbol["inclinacio"])
    return inclinaciones

inclinado = obtener_inclinaciones(a,"Jacarandá")

#%%


def especie_mas_inclinado(lista_arboles):
    """Combinando la función especies() con obtener_inclinaciones() escribí una
    función especimen_mas_inclinado(lista_arboles) que, dada una lista de árboles devuelva 
    la especie que tiene el ejemplar más inclinado y su inclinación."""
    especies= []
    incl = []
    for arbol in lista_arboles:
        especies.append(arbol["nombre_com"])
        incl.append(arbol["inclinacio"])
    print(f"La especie mas inclinada es el {especies[incl.index(max(incl))]} y su inclinacion es {max(incl)} ")

a = leer_parque(archivo,"CENTENARIO")
especie_mas_inclinado(a)

#%%

def obtener_parametro(lista_arboles,llave,valor,llave2):
    """Dado un diccionario y un par llave,valor me devuelve una lista con todos los valores
    de una segunda llave.
    
    Ej:lista de arboles, quiero los valores de altura(llave2) de toda la especie(llave1) que
    sea Eucalipto(valor 2)
    
    """
    resultado = []
    for arbol in lista_arboles:
        try:
            if arbol[llave] == valor:
                resultado.append(arbol[llave2])
        except KeyError:
            print("Llave no encontrada")
    return resultado



def especie_promedio_mas_inclinada(lista_arboles):
    """Volvé a combinar las funciones anteriores para escribir la función 
    especie_promedio_mas_inclinada(lista_arboles) que, dada una lista de árboles devuelva
    la especie que en promedio tiene la mayor inclinación y el promedio calculado"""
    especies_arboles = especies(lista_arboles)
    especies_incl = []
    especies_incl_prom = []
    #Genero una lista con cada especie y sus diferentes inclinaciones
    for especie in especies_arboles:
        especies_incl.append([especie,obtener_parametro(lista_arboles,"nombre_com",especie,"inclinacio")])
    #Calculo el promedio de todas las inclinaciones para cada especie
    import numpy as np
    for especie in especies_incl:
        prom=np.mean(especie[1])
        especies_incl_prom.append(prom)
    resultado=list(zip(especies_arboles,especies_incl_prom))
    print(f"La especie mas inclinada en promedio es la {especies_incl[especies_incl_prom.index(max(especies_incl_prom))][0]} y su valor es {max(especies_incl_prom)}")
    return resultado
#%%
"""¿Qué habría que cambiar para obtener la especie con un ejemplar más inclinado
 de toda la ciudad y no solo de un parque?

RTA: En vez de dar la lista de un parque dar la lista  completa , modificar la lectura de la
lista completa para que los valores los ponga en el formato correspondiente.

Se modifico la funcion leer_parque para que funcione con la opcion"todos"
la funcion para obtener la especie con un ejemplar más inclinado
 de toda la ciudad y no solo de un parque es especie_mas_inclinado :"""





#%%

"""
 ¿Podrías dar la latitud y longitud de ese ejemplar? 
 Si, lo haria modificando la funcion especie_mas_inclinado:

 """
def especie_mas_inclinado2(lista_arboles):
    """Combinando la función especies() con obtener_inclinaciones() escribí una
    función especimen_mas_inclinado(lista_arboles) que, dada una lista de árboles devuelva 
    la especie que tiene el ejemplar más inclinado y su inclinación."""
    especies= []
    incl = []
    lat = []
    long = []
    for arbol in lista_arboles:
        especies.append(arbol["nombre_com"])
        incl.append(arbol["inclinacio"])
        lat.append(arbol["lat"])
        long.append(arbol["long"])
    indice = incl.index(max(incl))
    print(f"La especie mas inclinada es el {especies[indice]} y su inclinacion es {max(incl)} y su latitud y longitud son: {lat[indice]} y {long[indice]} ")

a = leer_parque(archivo,"CENTENARIO")
especie_mas_inclinado2(a)

#%%
"""" ¿Y dónde se encuentra (lat,lon) el ejemplar más alto? ¿De qué especie es?"""

def especie_mas_alto2(lista_arboles):
    """Combinando la función especies() con obtener_inclinaciones() escribí una
    función especimen_mas_inclinado(lista_arboles) que, dada una lista de árboles devuelva 
    la especie que tiene el ejemplar más inclinado y su inclinación."""
    especies= []
    alt = []
    lat = []
    long = []
    for arbol in lista_arboles:
        especies.append(arbol["nombre_com"])
        alt.append(arbol["altura_tot"])
        lat.append(arbol["lat"])
        long.append(arbol["long"])
    indice = alt.index(max(alt))
    print(f"La especie mas alta es el {especies[indice]} y su altura es {max(alt)} y su latitud y longitud son: {lat[indice]} y {long[indice]} ")

a = leer_parque(archivo,"CENTENARIO")
especie_mas_alto2(a)

    
    
    
    
    
    
    


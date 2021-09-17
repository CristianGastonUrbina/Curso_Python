#!/usr/bin/env python3
#%%
import fileparse
import csv
def leer_camion(nombre_archivo):
    """abre un archivo con el contenido de un camión, lo lee y devuelve 
        la información como una lista de diccionarios."""
    with open(nombre_archivo, 'rt') as file:
        camion = fileparse.parse_csv(file,select =["nombre","cajones","precio"],types = [str,int,float])
    return camion


#%%
""" A partir de un conjunto de precios en un archivo , arma un diccionario
 donde las claves sean los nombres de frutas y verduras, y 
 los valores sean los precios por cajón."""
 
def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as file:
        precios = fileparse.parse_csv(file,types= [str,float], has_headers = False)
    return precios


#%%
"""3.13 
 Recibe una lista de cajones y un diccionario con
 precios como input y devuelve una lista de tuplas conteniendo la información mostrada
 en la tabla anterior.
"""
def hacer_informe(camion,precios,headers):
    #Camion es una lista de diccionarios
    #Precio es un diccionario
    informe = []
    cabecera = ""
    for i in headers:
        cabecera +=f"{i:>10s} "  #imprime cabecera de la tabla
    print (cabecera)
    i="-"
    print ((f"{i*10:>10} ")*4)
    for i in camion:
        fruta = i["nombre"]                 #recorro la fila de los datos y los imprimo
        cajon = i["cajones"]
        precio_Comp = i["precio"]
        precios = dict(precios)
        precio_Dif = precios[fruta] - precio_Comp
        tupla = (fruta,cajon,precio_Comp,precio_Dif)
        informe.append(tupla)
        print(f"{fruta:>10s} {cajon:>10d} {'$'+(str(precio_Comp)):>10s} {precio_Dif:>10.2f}")
    
    return informe


#%%
"""
Le cambio el nombre solo pq el ejercicio asi lo pide

"""

def f_principal(parametros):
    """
    Parameters
    ----------
    parametros : una lista con 3 datos
    
    parametros : una lista con 3 datos de los cuales uso dos:
    prametros [1]: iterable que contiene strings
        iterable de strings  con la informacion del camion comprado.
    parametros [2]:iterable que contiene strings
       iterable de strings Informacion de los precios de cada fruta.

    Returns
    -------
    Imprime en consola la lista con la informacion de los archivos y las cabeceras.

    """
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')    
    camion = leer_camion(parametros[1]) 
    precios = leer_precios(parametros[2])
    hacer_informe(camion,precios,headers)



#%%

    


#%%

if __name__ == "__main__":
    import sys
    f_principal(sys.argv)





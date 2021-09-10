#%%
"""
Vas a modificar el archivo informe_funciones.py de modo que todas las operaciones principales, incluyendo cálculos e impresión, sean llevados a cabo por una colección de funciones. Guarda la nueva versión en un archivo informe_funciones.py. Más específicamente:

Creá una función imprimir_informe(informe) que imprima el informe.
Cambiá la última parte del programa de modo que consista sólo en una serie de llamados a funciones, sin ningún cómputo.

"""
#%%
import fileparse
import csv
def leer_camion(nombre_archivo):
    """abre un archivo con el contenido de un camión, lo lee y devuelve 
        la información como una lista de diccionarios."""
    camion = fileparse.parse_csv(nombre_archivo,select =["nombre","cajones","precio"],types = [str,int,float])
    return camion


#%%
""" A partir de un conjunto de precios , arma un diccionario
 donde las claves sean los nombres de frutas y verduras, y 
 los valores sean los precios por cajón."""
 
def leer_precios(nombre_archivo):
    precios = fileparse.parse_csv(nombre_archivo,types= [str,float], has_headers = False)
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
        cabecera +=f"{i:>10s} "  
    print (cabecera)
    i="-"
    print ((f"{i*10:>10} ")*4)
    for i in camion:
        fruta = i["nombre"]
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

def informe_camion(camionete, preciasos):
    """
    Parameters
    ----------
    camionete : archivo css
        Archivo con la informacion del camion comprado.
    preciasos : archivo css
        Informacion de los precios de cada fruta.

    Returns
    -------
    Imprime en consola la lista con la informacion de los archivos y las cabeceras.

    """
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')    
    camion = leer_camion(camionete)
    precios = leer_precios(preciasos)
    hacer_informe(camion, precios,headers)



#%%





# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 18:55:54 2021

@author: Usuario
"""
import csv


def parse_csv(lista, select = None, types = None, has_headers = True,silence_errors = True):
    """
    Parameters
    ----------
    lista : Iterable de strtings
        lista de la cual se tomaran los datos.
        
    has_headers : boleano, optional
        Si es true, se entiende que el primer valor del iterable los nombres de los valores siguientes. The default is True.
        
    select : lista de strings, optional
        Solo usar si has_header es TRUE. Permite seleccionar solo algunas de las cabeceras
        para tener en cuenta en la lista final. Deben estar en orden
        
    types : lista de tipo de datos, optional
        Convierte los valores de las datos en los tipos seleccionados.
        La lista no debe ser mayor que la cantidad de valores y deben estar en orden
    
    silence_errors : boleano, optional
        Si es True, se escriben los mensaje de errores capturados. The default is True.

    Returns
    -------
    Si has_headers = True retorna una lista de diccionarios con las cabeceras como claves
    Si has_headers = False retorna una lista de tuplas con los valores

    """
    filas = csv.reader(lista)
    registros = []

    for i,fila in enumerate(filas): #chequeo si tiene cabeceras

        if i == 0:
            
            if has_headers: 
                encabezados = fila
                
            if select: #chequeo si se selecciono solo algunas de las cabeceras
            
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
                
            else:
                indices = []
            
        
        try:
            if not fila:    # Saltear filas vacías
                continue
            
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
    
            #Convierto datos
            if types:
                fila=[tipo(dato) for tipo,dato in zip(types,fila)]
                
            # Armar el diccionario/tupla
            if has_headers:
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
            else:
                registros.append(tuple(fila))
            #Atrapado de posibles errores
        except ValueError as e:
            if silence_errors!=True:
                print(f"Fila {i}: No pude convertir {fila}")
                print(f"Fila {i}: Motivo: {e}")
        except NameError:
            raise RuntimeError("Para seleccionar, necesito encabezados.")    
                  
    return registros

if __name__ =="__main__":
    with open('../Data/camion.csv', 'rt') as file:
        camion = parse_csv(file, types=[str,int,float])
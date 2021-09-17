# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 18:55:54 2021

@author: Usuario
"""

import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se puede modificar los tipos de los datos determinando el parametreo types que debe ser una lista de funciones de tipos.
    Se puede elegir si el archivo tiene cabecera o no, con el el parametro has_headers. De ser asi, se devolvera una lista de tuplas en vez de diccionarios
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        
        # Lee los encabezados del archivo
        
        if has_headers:
            encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
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
            except ValueError:
                continue

    return registros


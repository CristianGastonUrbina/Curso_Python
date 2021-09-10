# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 09:20:01 2021

@author: Cristian
"""

#%%
def busqueda_lineal_lordenada(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    i = 0     
    for z in lista:  # recorremos los elementos de la lista
        if z > e:
            return pos
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
        i += 1       
    return pos
#%%

def donde_insertar(lista, x,verbose = False):
    """
    Parameters
    ----------
    lista : list
        Lista ordenada.
    x : elemento
        elemento a buscar en la lista.

    Returns
    -------
    pos = int.
    La posición de ese elemento en la lista (si se encuentra en la lista) o la posición donde se podría insertar el elemento para que la lista permanezca ordenada (si no está en la lista).
    """
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    izq = 0
    der = len(lista) - 1
    encontrado = False
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            encontrado = True
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda

    if not encontrado:
        if lista[der] < x:
            return der +1
        else:
            return der

    return pos

#%%
def insertar(lista, x):
    """
    Parameters
    ----------
    lista : list
        Lista ordenada.
    x : elemento
        elemento a buscar en la lista.
    
    Returns
    -------
    pos = int.
    Si el elemento se encuentra en la lista solamente devuelve su posición; si no se encuentra en la lista, lo inserta en la posición correcta para mantener el orden. En este segundo caso, también debe devolver su posición.
    """
    pos = donde_insertar(lista, x)
    if pos >= len(lista):
        lista.insert(pos,x)
        return pos
    
    if x == lista[pos]:
        return pos
    else:
        lista.insert(pos,x)
    return pos
#%%
def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comp = 0
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
        comp += 1
    return pos,comp
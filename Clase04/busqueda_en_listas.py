# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 09:20:01 2021

@author: Cristian
"""

def buscar_u_elemento(lista,elemento):
    """reciba una lista y un elemento y devuelva la posición de la última aparición 
    de ese elemento en la lista (o -1 si el elemento no pertenece a la lista)."""
    largo = len(lista) -1
    for indice ,valor in enumerate(reversed(lista)): #Recorro de atras hacia adelante para optimizar
        if valor == elemento:
            return largo - indice
            break
    return -1

print(buscar_u_elemento([1,2,3,2,3,4],1))
print(buscar_u_elemento([1,2,3,2,3,4],2))
print(buscar_u_elemento([1,2,3,2,3,4],3))
print(buscar_u_elemento([1,2,3,2,3,4],5))
#%%

def buscar_n_elemento(lista,elemento):
    """reciba una lista y un elemento y devuelva la cantidad de veces que aparece 
    el elemento en la lista. """
    acum=0
    for i in lista:
        if i == elemento:
            acum+= 1
    return acum

print(buscar_n_elemento([1,2,3,2,3,4],1))
print(buscar_n_elemento([1,2,3,2,3,4],2))
print(buscar_n_elemento([1,2,3,2,3,4],3))
print(buscar_n_elemento([1,2,3,2,3,4],5))       
#%%

def maximo(lista):
    """Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos."""
    maximo = lista[0]
    for i in lista:
        if maximo < i:
            maximo = i
    return maximo 
    
print(maximo([1,2,7,2,3,4]))
print(maximo([1,2,3,4]))
print(maximo([-5,4]))
print(maximo([-5,-4]))

#%%

def minimo(lista):
    """Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos."""
    minimo = lista[0]
    for i in lista:
        if minimo > i:
            minimo = i
    return minimo 
    
print(minimo([1,2,7,2,3,4]))
print(minimo([1,2,3,4]))
print(minimo([-5,4]))
print(minimo([-5,-4]))


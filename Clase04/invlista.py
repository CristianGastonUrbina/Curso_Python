# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:04:05 2021

@author: Cristian
"""

def invertir_lista(lista):
    """Dada una lista, retorna una nueva lista igual a la lista invertida"""
    inv_lista=[]
    for valor in reversed(lista):
        inv_lista.append(valor)
    return inv_lista

print(invertir_lista([1, 2, 3, 4, 5]))
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))

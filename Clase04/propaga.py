# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:27:24 2021

@author: Cristian
"""



def propagar_derecha(lista,indice):
    """Propaga mi "fuego" a la derecha"""
    proximo = indice + 1
    try:
        while lista[proximo] == 0:
            lista[proximo] = 1
            proximo += 1
    except IndexError:
        pass
    return lista
       
       
       
def propagar_isquierda (lista,indice):
    """Propaga mi "fuego" a la isquierda"""
    proximo = indice - 1
    try:
        while lista[proximo] == 0:
            lista[proximo] = 1
            proximo -= 1
    except IndexError:
        pass
    return lista
    

def propagar(lista2):
    """Imaginate una fila con varios fósforos uno al lado del otro. Los fósforos pueden
    estar en tres estados: nuevos, prendidos fuego o ya gastados (carbonizados).
    Representaremos esta situación con una lista L con un elemento por fósforo, que en cada
    posición tiene un 0 (nuevo), un 1 (encendido) o un -1 (carbonizado).
    El fuego se propaga inmediatamente de un fósforo encendido a cualquier fósforo nuevo que 
    tenga a su lado. Los fósforos carbonizados no se encienden nuevamente. reciba un vector 
    con 0's, 1's y -1's y devuelva un vector en el que
    los 1's se propagaron a sus vecinos con 0"""
    lista = lista2.copy()
    for indice,fosforo in enumerate(lista):
        if fosforo == 1:
            propagar_derecha(lista,indice)
            propagar_isquierda(lista,indice)
    print(lista)
    
lista=[ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
propagar(lista)
propagar([ 0, 0, 0, 1, 0, 0])

#%%

lista_1 = [ 0, 0, 0, 1, 0, 0]
lista_2 = [ 0, 0, 0, 0, 0, -1]
lista_3 = [ 0, 0, 0, 0, 0, 1]
lista_4 = []
lista_5 = [ 0 for _ in range(1000) ] + [1]
lista_6 = [1] + [ 0 for _ in range(1000) ]
lista_7 = [ (i% 6)//2-1 for i in range(200) ]
lista_8 = [ -1*((i% 6)//2-1) for i in range(60) ]


propagada = propagar(lista_1)





propagada = propagar(lista_2)





propagada = propagar(lista_3)




propagada = propagar(lista_4)


propagada = propagar(lista_5)




propagada = propagar(lista_6)




propagada = propagar(lista_7)




propagada = propagar(lista_8)


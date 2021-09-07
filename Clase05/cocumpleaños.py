# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 07:55:22 2021

@author: Cristian
"""

"""aciendo miles de experimentos numéricos, estimá la probabilidad de que en un grupo de 30 personas elegidas al azar,
 dos cumplan años el mismo día. Escribí un programita que permita calcular esa probabilidad asumiendo que el año tiene 
 365 días."""
import random

def hay_duplicados(lista):
    seteo = set()
    for i in lista:
        if i in seteo:
            return True
        else:
            seteo.add(i)
    return False



def co_cumpleanios(personas):
     dias_cumple = [random.randint(1,365) for _ in range(personas)]
     return hay_duplicados(dias_cumple)
 

def prob_co_cumpleanios(N,personas):
    casos=[]
    for i in range(N):
        casos.append(co_cumpleanios(personas))
    G = sum(casos)
    prob = G/N
    print(f"Se realizarion {N} iteracion y la probabilidad de que {personas} cumplan el mismo dia es de {prob}")


N= 100000
personas = 22
prob_co_cumpleanios(N,personas)
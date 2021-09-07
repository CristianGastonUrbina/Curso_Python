# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 08:14:16 2021

@author: Cristian
"""


"""Teniendo en cuenta las reglas del Truco, estimá la probabilidad de obtener 31, 32 o 33 puntos de envido en una mano.
 ¿Son iguales estas tres probabilidades? ¿Por qué?"""


def calcular_tanto(a,b):
    figura = [10,11,12]
    if a in figura:
        if b in figura:
            return 20
        else:
            return b+20
    if b in figura:
        return a +20
    else:
        return a+b+20
    


def cantalo(mano):
    tanto = []
    figura = [10,11,12]
    #Hay envido?
    if mano[0][0] == mano [1][0]:
        tanto.append(calcular_tanto(mano[0][1],mano[1][1]))
    elif mano[0][0] == mano[2][0]:
        tanto.append(calcular_tanto(mano[0][1],mano[2][1]))
    elif mano[1][0] == mano[2][0]:
        tanto.append(calcular_tanto(mano[1][1],mano[2][1]))
    
    #Pasa el tanto
    if tanto != []:
        return max(tanto)
    else:
        
        return 0
 
 
 
def envido(N):
    import random
    palo =["oro","espada","copa","basto"]
    valor = [1,2,3,4,5,6,7,10,11,12]
    naipes = [(palos,valores) for palos in palo for valores in valor]
    envidos = [cantalo(random.sample(naipes,3)) for _ in range(N)]
    envidos_altos =[ 1 for i in envidos if i>30]
    G = sum(envidos_altos)
    prob = G/N
    print(f"Se realizarion {N} iteracion y la probabilidad de que se halla envido mayor a 30  es de {prob}")


N=100000
envido(N)
    

    
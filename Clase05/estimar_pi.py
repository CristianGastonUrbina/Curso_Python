# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 11:18:01 2021

@author: Cristian
"""

def generar_punto():
    #genera un punto x,y con x e y dentro 0 y 1
    import random
    x = random.random()
    y = random.random()
    punto = (x,y)
    return punto

def estimar_py(N):
    #esima el valor de pi utilizando el metodo de monte carlo con N iteraciones
    puntos = [generar_punto() for _ in range(N)]
    dentro_del_circulo=[True for x in puntos if x[0]**2 + x[1]**2 < 1]
    G = sum(dentro_del_circulo)
    prob = G/N*4
    print(f"Se realizarion {N} iteracion y el valor de pi calculado es de {prob}")
    
        
        
estimar_py(10000)
    
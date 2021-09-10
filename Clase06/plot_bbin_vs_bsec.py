# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 09:54:04 2021

@author: Usuario
"""
def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

#%%
import random

def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)


def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom


#%%
def graficar_experimento(experimento_promedio,m,k):
    import matplotlib.pyplot as plt
    import numpy as np
    
    largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
    comps_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
    
    for i, n in enumerate(largos):
        lista = generar_lista(n, m) # genero lista de largo n
        comps_promedio[i] = experimento_promedio(lista, m, k)
    
    # ahora grafico largos de listas contra operaciones promedio de búsqueda.
    plt.plot(largos,comps_promedio,label = str(experimento_promedio))
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.legend()


#%%



import bbin
def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += bbin.busqueda_binaria(lista, x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def graficar_bbin_vs_bseq(m, k,funcion1,funcion2):
    import matplotlib.pyplot as plt
    graficar_experimento(funcion1)
    graficar_experimento(funcion2)
    plt.title("Complejidad de la Búsq. binaria vs  Búsq secuencial")
    plt.xlim(0,25)
    plt.ylim(0,25)
    

    
    
    
    
    
    
    
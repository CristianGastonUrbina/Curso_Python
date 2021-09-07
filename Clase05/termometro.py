# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 15:54:39 2021

@author: Cristian
"""

#%%
"""Supongamos que una persona se compra un termómetro que mide la temperatura con un error aleatorio de distribución normal con media 0 y desvío estándar de 0.2 grados (error gaussiano). Si la temperatura real de la persona es de 37.5 grados, simulá usando normalvariate() (con mu y sigma adecuados) n valores medidos por el termómetro. Escribí una función llamada medir_temp(n) que simule n mediciones y las devuelva en una lista.

Escribí una función llamada resumen_temp(n) que realice una simulación de n temperaturas (usando la función medir_temp(n)) y devuelva una tupla con el valor máximo, el mínimo, el promedio y la mediana (en ese orden) de estas n mediciones. Guardá tu script en el archivo termometro.py."""


media =0
desvio_estandar = 0.2
temperatura_real = 37.5

def medir_temp(N):
    import random
    import numpy as np
    lista=[temperatura_real + random.normalvariate(0,0.2) for _ in range(N)]
    array = np.array(lista)
    np.savetxt('Temperaturas.csv', array)
    return lista

N=999

def resumen_temp(N):
    import statistics
    mediciones = medir_temp(N)
    maximo = max(mediciones)
    minimo = min(mediciones)
    promedio = statistics.mean(mediciones)
    mediana = statistics.median(mediciones)
    resultado = (maximo,minimo,promedio,mediana)
    return resultado
    
medir_temp(N)

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 07:15:38 2021

@author: Usuario
"""

#%%
#Ejercicio 7.12
import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    """
    Parameters
    ----------
    largo : entero
        Es el numero que decide que tan larga sera la cominata.

    Returns
    -------
    array
        Un array que va sumando paso a paso un numero al azar entre -1 y 2 
        de con "largo" cantidad de indices

    """
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()


    
def trayectoria(graficos,larga=False):
    """
    Parameters
    ----------
    graficos : array de caminatas
        array que contiene todas las caminatas realizadas.
        
    larga : TYPE, optional
        si es False se retorna el indice de la caminata mas corta
        si es True se retorna el indice de la caminata mas larga
        . The default is False.
    Returns
    -------
    res : entero
        Retorna el indice de la caminata que menos se aleja , la que mas se aleja si
        larga = True
    """
    valores_finales = [grafico[-1] for grafico in graficos] #Se toman solo los valores finales
    
    for i,valor in enumerate(valores_finales): #se calcula el modulo
        if valor < 0:
            valores_finales[i]= valor*-1
            
    if larga:
        res = valores_finales.index(max(valores_finales))
    else:
        res = valores_finales.index(min(valores_finales))
        
    return res


def caminatas_al_azar(N,G):
    """
    Parameters
    ----------
    N : numero entero positivo
        Cantidad de pasos de caminata.
    G : numero entero positivo
        Cantidad de caminatas realizadas.

    Returns
    -------
    Un ploteo con todas las caminatas realizadas en un grafico y las caminatas
    mas y menos alejadas en graficos aparte.

    """
    graficos = []
    for i in range(G): #ploteo todos los graficos juntos
        plt.subplot(2, 1, 1)
        graficos.append(randomwalk(N))
        plt.plot(graficos[i-1])
        plt.ylabel('distancia al origen')
        plt.title("12 Caminatas al azar")
        plt.xticks([])
        plt.xlim(0,N)
        plt.ylim(-700,700)

    mas_larga = trayectoria(graficos,larga=True)#obtengo las caminatas mas y menos lejanas
    mas_corta = trayectoria(graficos)
    
    plt.subplot(2, 2, 3)#Ploteo la mas lejana
    plt.plot(graficos[mas_larga])
    plt.title("La que mas se aleja")
    plt.xticks([])
    plt.xlim(0,N)
    plt.ylim(-700,700)
    
    plt.subplot(2, 2, 4)#Ploteo la mas cercana
    plt.plot(graficos[mas_corta])
    plt.title("La que menos se aleja")
    plt.xticks([])
    plt.xlim(0,N)
    plt.ylim(-700,700)
    
    plt.show()


if __name__=="__main__" :
    N = 100000
    numero_graficos = 12
    caminatas_al_azar(N,numero_graficos)

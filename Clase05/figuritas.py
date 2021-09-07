# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 18:38:27 2021

@author: Cristian
"""
import matplotlib.pyplot as plt
import numpy as np
import random
figus_total=670

def crear_album(cantidad_de_figus):
    album = np.zeros(cantidad_de_figus,dtype=np.int64)
    return album


def album_incompleto(album):
    return  album.sum()!=figus_total
  

def comprar_figus(figus_total):
    figu_comprada = random.randint(0,figus_total-1)
    return figu_comprada

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    acum = 0
    while album_incompleto(album) == True:
        acum+= 1
        album[comprar_figus(figus_total)]=1
    return acum


n_repeticiones = 1000

def experimento_figus(n_repeticiones, figus_total):
    experimentos = [cuantas_figus(figus_total) for _ in range(n_repeticiones)]
    return (np.mean(experimentos))

def comprar_paquete(figus_total,figus_paquete):
    paquete_comprado = [random.randint(0,figus_total-1) for _ in range(figus_paquete)]
    return paquete_comprado
    
figus_paquete = 5

def pegar_figus(paquete,album):
    for i in paquete:
        album[i]=1
    return album
    
    
    

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    acum = 0
    while album_incompleto(album) == True:
        acum+= 1
        paquete = comprar_paquete(figus_total, figus_paquete)
        pegar_figus(paquete, album)
    return acum    

def experimento_paquetes(n_repeticiones, figus_total,figus_paquete):
    resultados = [cuantos_paquetes(figus_total,figus_paquete) for _ in range(n_repeticiones)]
    return (np.mean(resultados))



def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()

#%%
"""Utilizando lo implementado en el ítem anterior, estimá la probabilidad de completar el álbum con 850 paquetes o menos."""

def llenado_con_menos_de(npaquetes,n_repeticiones):
    resultado = [cuantos_paquetes(figus_total,figus_paquete) for _ in range(n_repeticiones) ]
    resultadoOK = [1 for i in resultado if i<=npaquetes]
    G=sum(resultadoOK)
    prob = G/n_repeticiones
    return prob
    
    
    

npaquetes=850
a  = [cuantos_paquetes(figus_total,figus_paquete) for _ in range(n_repeticiones)]

plt.hist(a,bins=25)
plt.show()
    


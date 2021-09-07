# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 20:43:45 2021

@author: Cristian
"""

import random
dados = 5
def tirada(dados):
    """Genera una lista con "dados" cantidad de elementos al azar entre 1 y 6"""
    tirada = [random.randint(1,6) for _ in range(dados) ]
    return tirada

def es_generala (tirada):
    return (max(tirada)==min(tirada))
N=100000

tiradas = [es_generala(tirada(5)) for _ in range(N) ]
G = sum(tiradas)

prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

#%%

"""Escribí una función llamada prob_generala(N) que, a partir de un parámetro N y usando las funciones del Ejercicio 5.1 
realice una simulación con N repeticiones, para estimar la probabilidad de obtener una generala al finalizar una mano de
 tres tiradas. La función debe devolver un número entre 0 y 1. Guardala en un archivo generala.py para el cierre de la clase.

Extra: Hay gente que, si en la primera tirada le salen todos dados diferentes, los mete al cubilete y tira los cinco
 nuevamente. Otras personas, eligen uno de esos dados diferentes, lo guardan, y tiran sólo los cuatro restantes. 
 ¿Podés determinar, por medio de simulaciones, si hay una de estas estrategias que sea mejor que la otra?"""

def intento_generala (tiro):
    """Dado un array se fija cual es el numero que mas se repite, guarda esos numero y genera
    array nuevo con los numeros viejos mas los numeros restantes"""
    #Determino cual es numero que se repite mas
    repes = [tiro.count(i+1) for i in range(6) ]
    numero_a_buscar = repes.index(max(repes))+1
    #guardo mis dados 
    dados_guardados = [numero_a_buscar for _ in range(repes[numero_a_buscar - 1])] 
    #agrego dados nuevos
    nueva_tirada = dados_guardados + [random.randint(1,6) for _ in range(5-len(dados_guardados))]
    return nueva_tirada

  


def prob_generala(N):
    tiradas = []
    for i in range(N):
        tiro = tirada(5)
        tirada2 = intento_generala(tiro)
        tirada3 = intento_generala(tirada2)
        tiradas.append(es_generala(tirada3))
    G = sum(tiradas)
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
    return


N=100000
prob_generala(N)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
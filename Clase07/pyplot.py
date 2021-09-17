# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 07:15:38 2021

@author: Usuario
"""
"""
from matplotlib import pyplot as plt
import numpy as np
X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
S = np.sin(X)

plt.plot(X,C)
plt.plot(X,S)


# Crea una figura nueva, de 8x6 pulgadas, con 80 puntos por pulgada
plt.figure(figsize=(8, 6), dpi=80)

# Crea un nuevo subplot, en una grilla de 1x1
plt.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

# Plotea el coseno con una línea azul contínua de ancho 1 (en pixeles)
plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# Plotea el seno con una línea verde contínua de ancho 1 (en pixeles)
plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")

# Rango del eje x
plt.xlim(-4.0, 4.0)

# Ponemos marcas (ticks) en el eje x
plt.xticks(np.linspace(-4, 4, 9))

# Rango del eje y
plt.ylim(-1.0, 1.0)

# Ponemos marcas (ticks) en el eje y
plt.yticks(np.linspace(-1, 1, 5))

# Podemos grabar el gráfico (con 72 dpi)
# plt.savefig("ejercicio_2.jpeg)", dpi=72)

# Mostramos el resultado en pantalla
plt.show()"""
#%%
#Ejercicio 7.11
"""
fig = plt.figure()
plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas

plt.subplot(2, 3, 4) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5)
plt.plot([0,1],[0.5,0.5])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 6) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

plt.show()"""
#%%
#Ejercicio 7.12
import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()
    
def trayectoria(graficos,larga=False):
    valores_finales = [grafico[-1] for grafico in graficos]
    
    for i,valor in enumerate(valores_finales):
        if valor < 0:
            valores_finales[i]= valor*-1
    if larga:
        res = valores_finales.index(max(valores_finales))
    else:
        res = valores_finales.index(min(valores_finales))
    return res

def caminatas_al_azar(N,G):
    graficos = []
    for i in range(G):
        plt.subplot(2, 1, 1)
        graficos.append(randomwalk(N))
        plt.plot(graficos[i-1])
        plt.ylabel('distancia al origen')
        plt.title("12 Caminatas al azar")
        plt.xticks([])
        plt.xlim(0,N)
        plt.ylim(-700,700)

    mas_larga = trayectoria(graficos,larga=True)
    mas_corta = trayectoria(graficos)
    
    plt.subplot(2, 2, 3)
    plt.plot(graficos[mas_larga])
    plt.title("La que mas se aleja")
    plt.xticks([])
    plt.xlim(0,N)
    plt.ylim(-700,700)
    
    plt.subplot(2, 2, 4)
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

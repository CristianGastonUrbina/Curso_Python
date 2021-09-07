# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 10:44:13 2021

@author: Cristian
"""

def encabezado(numeroMaximo):
    impresion = f"{' ':<8}"
    for i in range(numeroMaximo):
        impresion += f"{i:<4}" 
    print(impresion)
    
def lineado(lineas):
    print(f"{'-'*lineas}")

def cuerpoTabla(limiteTabla,numero):
    impresion = ""
    for i in range(limiteTabla+1):
        if i == 0:
            impresion += f"{str(numero)+':':<8}"
        else:
            impresion += f"{numero*(i-1):<4}"
    print(impresion)


def hacerTabla(limiteTabla):
    encabezado(limiteTabla+1)
    lineado((limiteTabla*4)+10)
    for i in range(10):
       cuerpoTabla(limiteTabla+1,i)    

hacerTabla(9)




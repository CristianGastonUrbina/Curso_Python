# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 19:50:44 2021

@author: Usuario
"""

def valor_absoluto(n):
    """
    Parameters
    ----------
    n : numero
        numero al cual se le calculara el valor absoluto.

    Returns
    -------
    El modulo de n
    """
    if n >= 0:
        return n
    else:
        return -n
    
    #%%
    def suma_pares(l):
        """
        Parameters
        ----------
        l : lista
            lista de numeros.

        Returns
        -------
        res : int
            La suma de todos los numeros pares dentro de l
        """
        res = 0
        for e in l:
            if e % 2 ==0: #Chequeo que el numero sea par
                res += e
            else:
                res += 0
    
        return res
#Invariante res:la suma de todos los numeros pares hasta el indice e de la lista l
#%%
def veces(a, b):
    """
    Parameters
    ----------
    a : numero entero positivo
    b : numero entero positivo

    Returns res : la multiplicacion de a  por b
    """
    res = 0
    nb = b
    while nb != 0:
        res += a 
        nb -= 1     
    return res
 #invariante = res : la suma de a+a b-nb veces 
#%%
def collatz(n):
    """
    Parameters
    ----------
    n : numero entero positivo

    Returns
    -------
    res :la cantidad de pasos que se realizaron dentro de la conjetura de collatz
    """
    res = 1

    while n!=1:
        if n % 2 == 0:   # si n es par, n= n/2
            n = n//2
        else:
            n = 3 * n + 1 # si n es impar hago n =3*(n+1)
        res += 1

    return res
#invariante res : La cantidad de veces que realice la conjetura hasta el momento
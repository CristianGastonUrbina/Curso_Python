# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 18:22:08 2021

@author: Cristian
"""
import numpy as np
temperaturas = np.loadtxt("../Data/Temperaturas.csv")

def plotear_temperaturas(archivo):
    import matplotlib.pyplot as plt
    plt.hist(temperaturas,bins=50)
    plt.show()

plotear_temperaturas(temperaturas)
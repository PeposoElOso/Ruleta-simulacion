
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
import collections as col


def ruleta(n_tiradas, ronda):
    numeros = np.random.randint(0, 37, size=(ronda, n_tiradas))
    return numeros.tolist()


def estadisticas(numeros, apuesta):

    # Convertir la lista de listas en un DataFrame
    df = pd.DataFrame(numeros)
    
    # Calcular la media y la desviación estándar
    media = df.mean().mean()
    desviacion = df.std().std()
    
    # Calcular la frecuencia absoluta
    frecuencia_absoluta = (df == apuesta).sum().sum()
    
    # Calcular la frecuencia relativa
    frecuencia_relativa = (frecuencia_absoluta / (df.size)) * 100
    
    #Calcular la moda 
    datos_flat = [num for sublist in numeros for num in sublist]  # aplana la lista 2D
    conteo = col.Counter(datos_flat)
    max_freq = max(conteo.values())
    moda = [num for num, freq in conteo.items() if freq == max_freq]
    
    #Calcular cantidad de nros par
    impar = [num for num in datos_flat if num % 2 != 0]
    par = [num for num in datos_flat if num % 2 == 0]
    cantidad_impar = len(impar)
    cantidad_par = len(par)
    porcentaje_impar = (cantidad_impar / len(datos_flat)) * 100
    porcentaje_par = (cantidad_par / len(datos_flat)) * 100

    return media, desviacion, frecuencia_absoluta, frecuencia_relativa, numeros, moda, cantidad_par, cantidad_impar, porcentaje_impar, porcentaje_par



def aplanar(numeros):
    return [num for ronda in numeros for num in ronda]



def frecuencia_absoluta(tiros, numero):
    return tiros.count(numero)



def frecuencia_moda(tiros):
    conteo = col.Counter(tiros)
    max_freq = max(conteo.values())
    modas = [num for num, freq in conteo.items() if freq == max_freq]
    return modas[0], max_freq



def desviacion_std(tiros):
    return np.std(tiros)

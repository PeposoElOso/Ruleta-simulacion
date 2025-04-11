
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
import collections as col


def ruleta(n_tiradas, ronda):
    numeros = np.random.randint(0, 37, size=(ronda, n_tiradas))
    return numeros.tolist()


def moda(numeros, apuesta):
    # Aplanamos todos los datos
    datos_flat = [num for sublist in numeros for num in sublist]

    # Calculamos la moda global
    conteo = col.Counter(datos_flat)
    max_freq = max(conteo.values())
    moda = [num for num, freq in conteo.items() if freq == max_freq][0]  # tomamos la primera si hay más de una

    # Frecuencia acumulada
    acumulado = []
    freq_moda = []
    freq_apuesta = []

    for i in range(1, len(datos_flat) + 1):
        sublista = datos_flat[:i]
        freq_moda.append(sublista.count(moda))
        freq_apuesta.append(sublista.count(apuesta))
        acumulado.append(i)

    return moda, acumulado, freq_moda, freq_apuesta




def media(numeros):
    # Convertir la lista de listas en un DataFrame
    df = pd.DataFrame(numeros)
    
    # Calcular la media 
    media = df.mean().mean()
    
    return media

def desviacion_acumulada(numeros):
    datos_flat = [num for sublist in numeros for num in sublist]
    desvios = []

    for i in range(1, len(datos_flat) + 1):
        sublista = datos_flat[:i]
        desvio = np.std(sublista)
        desvios.append(desvio)

    return desvios


def frecuencia_absoluta_acumulada(numeros, apuesta):
    datos_flat = [num for sublist in numeros for num in sublist]
    frecuencias = []

    for i in range(1, len(datos_flat) + 1):
        sublista = datos_flat[:i]
        cuenta = sublista.count(apuesta)
        frecuencias.append(cuenta)

    return frecuencias


def frecuencia_relativa(numeros, apuesta):
    datos_flat = [num for sublist in numeros for num in sublist]
    total_tiradas = []
    frecuencia_relativa = []

    for i in range(1, len(datos_flat) + 1):
        sublista = datos_flat[:i]
        cuenta = sublista.count(apuesta)
        frecuencia = (cuenta / i) * 100
        total_tiradas.append(i)
        frecuencia_relativa.append(frecuencia)

    return total_tiradas, frecuencia_relativa



def paridad(numeros):
    # Convertir la lista de listas en un DataFrame
    df = pd.DataFrame(numeros)
    
    # Calcular la cantidad de números pares e impares
    cantidad_pares = (df % 2 == 0).sum().sum()
    cantidad_impares = (df % 2 != 0).sum().sum()
    
    return cantidad_pares, cantidad_impares
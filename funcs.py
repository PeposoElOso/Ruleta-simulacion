
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
import collections as col

rojo = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
negro = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

columna1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
columna2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
columna3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

fila1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
fila2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
fila3 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
def ruleta(n_tiradas, ronda):
    numeros = np.random.randint(0, 37, size=(ronda, n_tiradas))
    return numeros.tolist()

def color(numeros):
    colores = [["" for _ in range(len(numeros[0]))] for _ in range(len(numeros))] 
    for i in range(len(numeros)):
        for j in range(len(numeros[i])):
            if numeros[i][j] == 0:
                colores[i][j] = "verde"
            elif numeros[i][j] in rojo: 
                colores[i][j] = "rojo"  
            else:
                colores[i][j] ="negro"
                
    return colores

def columna(numeros, columna):
    columna = [[""for _ in range(len(numeros[0]))] for _ in range(len(numeros))]
    for i in range(len(numeros)):
        for j in range(len(numeros[i])):
            if numeros[i][j] in columna1:
                columna[i][j] = "columna1"
            elif numeros[i][j] in columna2:
                columna[i][j] = "columna2"
            elif numeros[i][j] in columna3:
                columna[i][j] = "columna3"
            else:
                columna[i][j] = "no pertenece a ninguna columna"
                
    return columna




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




def media_acumulada(numeros):
    datos_flat = [num for sublist in numeros for num in sublist]
    medias = []

    for i in range(1, len(datos_flat) + 1):
        sublista = datos_flat[:i]
        media = np.mean(sublista)
        medias.append(media)

    return medias


def desviacion_acumulada(numeros):
    datos_flat = [num for sublist in numeros for num in sublist]
    desvios = []

    for i in range(1, len(datos_flat) + 1):
        sublista = datos_flat[:i]
        desvio = np.std(sublista)
        desvios.append(desvio)

    return desvios

def frecuencia_absoluta_por_numero(numeros):
    # Aplanamos todos los datos
    datos_flat = [num for sublist in numeros for num in sublist]

    # Contamos la frecuencia de cada número
    conteo = col.Counter(datos_flat)

    # Convertimos el conteo a un DataFrame para facilitar la visualización
    df_frecuencia = pd.DataFrame(conteo.items(), columns=['Número', 'Frecuencia'])
    df_frecuencia.sort_values(by='Número', inplace=True)

    return df_frecuencia

def frecuencia_relativa_por_ronda(numeros, apuesta):
    frecuencias_relativas = []

    for ronda in numeros:
        acumuladas = []
        contador = 0
        for i in range(1, len(ronda) + 1):
            if ronda[i - 1] == apuesta:
                contador += 1
            acumuladas.append((contador / i) * 100)  # porcentaje
        frecuencias_relativas.append(acumuladas)

    return frecuencias_relativas

    

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

def medias_acumuladas_por_ronda(numeros):
    medias_por_ronda = []
    for ronda in numeros:
        acumulado = []
        suma = 0
        for i, valor in enumerate(ronda):
            suma += valor
            media_actual = suma / (i + 1)
            acumulado.append(media_actual)
        medias_por_ronda.append(acumulado)
    return medias_por_ronda

def desviaciones_acumuladas_por_ronda(numeros):
    desviaciones_por_ronda = []
    for ronda in numeros:
        acumulado = []
        for i in range(1, len(ronda)+1):
            sub_ronda = ronda[:i]
            desviacion_actual = np.std(sub_ronda)
            acumulado.append(desviacion_actual)
        desviaciones_por_ronda.append(acumulado)
    return desviaciones_por_ronda

def frecuencia_absoluta_apuesta_por_ronda(numeros, apuesta):
    frecuencias_por_ronda = []
    for ronda in numeros:
        acumulado = []
        contador = 0
        for i in range(1, len(ronda) + 1):
            if ronda[i - 1] == apuesta:
                contador += 1
            acumulado.append(contador)
        frecuencias_por_ronda.append(acumulado)
    return frecuencias_por_ronda

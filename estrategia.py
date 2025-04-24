import pandas as pd
import matplotlib.pyplot as plt
from funcs import ruleta, color   
 
saldo_inicial = 10000
apuesta_base = 100

def martingala():
    color_apostado = 'r'   
    saldo_actual = saldo_inicial
    apuesta_actual = apuesta_base
    historial = []

    # Generamos tiradas de la ruleta
    n_tiradas = 100
    tiradas = ruleta(n_tiradas, 1)[0]
    colores = color([tiradas])[0]  # devuelve ["rojo", "negro", 

    for i in range(len(colores)):
        if saldo_actual <= 0 or apuesta_actual > saldo_actual:
            print(f"Saldo insuficiente para continuar en la ronda {i+1}.")
            break

        resultado_color = colores[i]
        color_real = 'rojo' if color_apostado == 'r' else 'negro'


        if resultado_color == color_real:
            saldo_actual += apuesta_actual
            historial.append((i+1, tiradas[i], resultado_color, apuesta_actual, saldo_actual, 'GANÓ'))
            apuesta_actual = apuesta_base  # Reinicia al monto base
        else:
            saldo_actual -= apuesta_actual
            historial.append((i+1, tiradas[i], resultado_color, apuesta_actual, saldo_actual, 'PERDIÓ'))
            apuesta_actual *= 2  # Duplicar al perder

    # Resultados finales
    df_resultados = pd.DataFrame(historial, columns=["Ronda", "Número", "Color", "Apuesta", "Saldo", "Resultado"])
    print("\n--- RESULTADOS MARTINGALA ---")
    print(df_resultados)

    # Gráfica de evolución
    plt.plot(df_resultados["Ronda"], df_resultados["Saldo"], marker='o')
    plt.title("Evolución del Saldo - Martingala")
    plt.xlabel("Ronda")
    plt.ylabel("Saldo")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return df_resultados

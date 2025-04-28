import random
import funcs as f
import graf as gr
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from funcs import ruleta, color


balance = 20  # Dinero inicial
apuesta = 10  # Apuesta base


def dalembert(colores, balance, color_apuesta, numeros):
    bet = apuesta
    balance_inicial = balance
    historial = []
    contador = 0
    salir = False
    historial_rondas = []
    fa_ronda = 0
    print(f"Color de apuesta: {color_apuesta}")
    print(f"Balance inicial: {balance}")

    for i in range(len(colores)):
        for j in range(len(colores[i])):
            contador = contador + 1
            if balance <= 0 or bet > balance:
                print("Saldo insuficiente.")
                salir = True
                break

            else:
                if colores[i][j] == color_apuesta:
                    balance += bet
                    historial.append(
                        (contador, numeros[i][j], colores[i][j], bet, balance, "GANÓ")
                    )
                    fa_ronda = fa_ronda + 1
                    bet = max(apuesta, bet - apuesta)  # Reducir apuesta
                else:
                    balance -= bet
                    historial.append(
                        (contador, numeros[i][j], colores[i][j], bet, balance, "PERDIÓ")
                    )
                    bet += apuesta  # Incrementar apuesta

        historial_rondas.append((i, fa_ronda))
        fa_ronda = 0
        if salir:
            for i in range(len(colores)):
                historial_rondas.append((i, fa_ronda))

            break
    print(f"Balance final: {balance}")

    # Resultados finales
    df_resultados = pd.DataFrame(
        historial, columns=["Ronda", "Número", "Color", "Apuesta", "Saldo", "Resultado"]
    )
    print("\n--- RESULTADOS Dalembert ---")
    print(df_resultados)

    # Gráfica de evolución
    plt.axhline(balance_inicial, linestyle="--", color="red")
    plt.plot(df_resultados["Ronda"], df_resultados["Saldo"])
    plt.title("Evolución del Saldo - Dalembert")
    plt.xlabel("Ronda")
    plt.ylabel("Saldo")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    resultados = pd.DataFrame(historial_rondas, columns=["Ronda", "Frecuencia"])
    plt.figure(figsize=(10, 6))
    plt.title("\n--- Frecuencia Absoluta Velazquez ---")

    plt.bar(
        resultados["Ronda"],
        resultados["Frecuencia"],
        color="skyblue",
        label="Frecuencia Absoluta",
    )
    plt.title("Frecuencia Absoluta por ronda")
    plt.xlabel("Ronda")
    plt.ylabel("Frecuencia")
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    apuestas_vs_saldo(df_resultados, "Dalembert")
    evolucion_ganancias_perdidas(df_resultados, "Dalembert")
    porcentaje_rondas_ganadas(historial_rondas, tiros_por_ronda=len(numeros[1]))

    return df_resultados


##############################################################################################################################################################################################


def velazquez(colores, balance, color_apuesta, numeros):
    balance_inicial = balance
    bet = apuesta
    historial = []
    contador = 0
    salir = False
    historial_rondas = []
    fa_ronda = 0

    print(f"Balance inicial: {balance}")
    for i in range(len(colores)):
        for j in range(len(colores[i])):
            contador = contador + 1
            if balance <= 0 or bet > balance:
                print("Saldo insuficiente.")
                salir = True
                break

            else:
                if colores[i][j] == color_apuesta:
                    balance += bet
                    fa_ronda = fa_ronda + 1
                    historial.append(
                        (contador, numeros[i][j], colores[i][j], bet, balance, "GANÓ")
                    )
                    bet = max(apuesta, bet / 2)  # divide apuesta
                else:
                    balance -= bet
                    historial.append(
                        (contador, numeros[i][j], colores[i][j], bet, balance, "PERDIÓ")
                    )
                    bet += bet * 2  # duplica apuesta

        historial_rondas.append((i, fa_ronda))
        fa_ronda = 0
        if salir:
            for i in range(len(colores)):
                historial_rondas.append((i, fa_ronda))

            break
    print(f"Balance final: {balance}")

    # Resultados finales
    df_resultados = pd.DataFrame(
        historial, columns=["Ronda", "Número", "Color", "Apuesta", "Saldo", "Resultado"]
    )
    print("\n--- RESULTADOS Velazquez ---")
    print(df_resultados)

    # Gráfica de evolución
    plt.plot(df_resultados["Ronda"], df_resultados["Saldo"])
    plt.axhline(balance_inicial, linestyle="--", color="red")
    plt.title("Evolución del Saldo - Velazquez")
    plt.xlabel("Ronda")
    plt.ylabel("Saldo")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    resultados = pd.DataFrame(historial_rondas, columns=["Ronda", "Frecuencia"])
    plt.figure(figsize=(10, 6))
    plt.title("\n--- Frecuencia Absoluta Velazquez ---")

    plt.bar(
        resultados["Ronda"],
        resultados["Frecuencia"],
        color="skyblue",
        label="Frecuencia Absoluta",
    )
    plt.title("Frecuencia Absoluta por ronda")
    plt.xlabel("Ronda")
    plt.ylabel("Frecuencia")
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    apuestas_vs_saldo(df_resultados, "Velazquez")
    evolucion_ganancias_perdidas(df_resultados, "Velazquez")
    porcentaje_rondas_ganadas(historial_rondas, tiros_por_ronda=len(numeros[1]))

    return df_resultados


########################################################################################################################################################################################


def martingala(colores, balance, color_apuesta, numeros):
    apuesta = 10
    bet = apuesta
    historial = []
    contador = 0
    balance_inicial = balance
    historial_rondas = []
    fa_ronda = 0
    salir = False
    print(f"Balance inicial: {balance}")

    for i in range(len(colores)):
        for j in range(len(colores[i])):
            contador = contador + 1

            if balance <= 0 or bet > balance:
                print(f"Saldo insuficiente para continuar en la ronda {contador}.")
                salir = True
                break

            if colores[i][j] == color_apuesta:
                balance += bet
                fa_ronda = fa_ronda + 1
                historial.append(
                    (contador, numeros[i][j], colores[i][j], bet, balance, "GANÓ")
                )
                bet = apuesta  # Reinicia al monto base
            else:
                balance -= bet
                historial.append(
                    (contador, numeros[i][j], colores[i][j], bet, balance, "PERDIÓ")
                )
                bet *= 2  # Duplicar al perder

        historial_rondas.append((i, fa_ronda))
        fa_ronda = 0
        if salir:
            for i in range(len(colores)):
                historial_rondas.append((i, fa_ronda))

            break

    # Resultados finales
    df_resultados = pd.DataFrame(
        historial, columns=["Ronda", "Número", "Color", "Apuesta", "Saldo", "Resultado"]
    )
    print("\n--- RESULTADOS MARTINGALA ---")
    print(df_resultados)

    # Gráfica de evolución
    plt.plot(df_resultados["Ronda"], df_resultados["Saldo"])
    plt.axhline(balance_inicial, linestyle="--", color="red")
    plt.title("Evolución del Saldo - Martingala")
    plt.xlabel("Ronda")
    plt.ylabel("Saldo")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    resultados = pd.DataFrame(historial_rondas, columns=["Ronda", "Frecuencia"])
    plt.figure(figsize=(10, 6))
    plt.title("\n--- Frecuencia Absoluta Martindale ---")

    plt.bar(
        resultados["Ronda"],
        resultados["Frecuencia"],
        color="skyblue",
        label="Frecuencia Absoluta",
    )
    plt.title("Frecuencia Absoluta por ronda")
    plt.xlabel("Ronda")
    plt.ylabel("Frecuencia")
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    apuestas_vs_saldo(df_resultados, "Martingala")
    evolucion_ganancias_perdidas(df_resultados, "Martingala")
    porcentaje_rondas_ganadas(historial_rondas, tiros_por_ronda=len(numeros[1]))

    return df_resultados


########################################################################################################################################################################################
def fibonacci(colores, balance, color_apuesta,numeros):
    i = 0
    multiplicador_de_apuesta = 1
    bet = apuesta * multiplicador_de_apuesta
    balance_inicial = balance
    salir = False
    contador = 0
    fa_ronda = 0
    historial = []  
    historial_rondas = []
    for i in range(len(colores)):
        for j in range(len(colores[i])):
            contador = contador + 1
            
            
            if balance <= 0 or bet > balance:
                print(f"Saldo insuficiente en la tirada {j} de la ronda {i}.")
                salir = True
                break

            else:
                print(
                    f"Apuesta en la tirada {j + 1} de la ronda {i + 1}: ApuestaInicial:{apuesta} * MultiplicadorFibonacci:{multiplicador_de_apuesta} = ${bet}"
                )
                if colores[i][j] == color_apuesta:
                    print("Ganó: $", bet)
                    fa_ronda = fa_ronda + 1
                    historial.append((contador, numeros[i][j], colores[i][j], bet, balance, "GANÓ"))
                    balance += bet
                    multiplicador_de_apuesta = aumentar_apuesta(
                        multiplicador_de_apuesta, True
                    )
                    bet = apuesta * multiplicador_de_apuesta  # Reducir apuesta
                else:
                    print("Perdió: $", bet)
                    balance -= bet
                    historial.append((contador, numeros[i][j], colores[i][j], bet, balance, "PERDIÓ"))
                    multiplicador_de_apuesta = aumentar_apuesta(
                        multiplicador_de_apuesta, False
                    )
                    bet = apuesta * multiplicador_de_apuesta  # Incrementar apuesta
            print("Saldo: $", balance)
        historial_rondas.append((i, fa_ronda))
        fa_ronda = 0
        if salir:
            for i in range(len(colores)):
                historial_rondas.append((i, fa_ronda))
        
        
    df_resultados = pd.DataFrame(
    historial, columns=["Ronda", "Número", "Color", "Apuesta", "Saldo", "Resultado"]
    )
    print("\n--- RESULTADOS FIBONACCI ---")
    print(df_resultados)

    # Gráfica de evolución
    plt.plot(df_resultados["Ronda"], df_resultados["Saldo"])
    plt.axhline(balance_inicial, linestyle="--", color="red")
    plt.title("Evolución del Saldo - FIBONACCI")
    plt.xlabel("Ronda")
    plt.ylabel("Saldo")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    resultados = pd.DataFrame(historial_rondas, columns=["Ronda", "Frecuencia"])
    plt.figure(figsize=(10, 6))
    plt.title("\n--- Frecuencia Absoluta Martindale ---")

    plt.bar(
        resultados["Ronda"],
        resultados["Frecuencia"],
        color="skyblue",
        label="Frecuencia Absoluta",
    )
    plt.title("Frecuencia Absoluta por ronda")
    plt.xlabel("Ronda")
    plt.ylabel("Frecuencia")
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.legend()
    plt.tight_layout()
    plt.show()

    if balance > 0:
        print("Dinero final: $", balance)
    else:
        print("Te has quedado sin dinero en la ronda ", i)
        
    apuestas_vs_saldo(df_resultados, "Fibonacci")
    evolucion_ganancias_perdidas(df_resultados, "Fibonacci")
    porcentaje_rondas_ganadas(historial_rondas, tiros_por_ronda=len(numeros[1]))



def aumentar_apuesta(valor_inicial: int, retroceder: bool) -> int:
    fib = [1, 1]
    while fib[-1] < valor_inicial:
        fib.append(fib[-1] + fib[-2])

    if valor_inicial not in fib:
        raise ValueError(
            "El número inicial debe pertenecer a la sucesión de Fibonacci."
        )

    # Buscar el último índice del valor (por si hay repetidos, como los dos 1s)
    indices = [i for i, v in enumerate(fib) if v == valor_inicial]
    idx = indices[-1]  # el último índice donde aparece el valor

    if retroceder:
        if idx < 2:
            return fib[0]  # valor mínimo permitido
        return fib[idx - 2]
    else:
        while idx + 1 >= len(fib):
            fib.append(fib[-1] + fib[-2])
        return fib[idx + 1]





def apuestas_vs_saldo(df_resultados, estrategia):
    
    df_resultados["Apuesta Acumulada"] = df_resultados["Apuesta"].cumsum()

    plt.figure(figsize=(10,6))
    plt.plot(df_resultados["Apuesta Acumulada"], df_resultados["Saldo"],)
    plt.title(f"Apuestas Acumuladas vs Saldo - {estrategia}")
    plt.xlabel("Apuestas Acumuladas ($)")
    plt.ylabel("Saldo ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def evolucion_ganancias_perdidas(df_resultados, estrategia):
  
    
    df_resultados["Ganado"] = df_resultados.apply(lambda x: x["Apuesta"] if x["Resultado"] == "GANÓ" else 0, axis=1)
    df_resultados["Perdido"] = df_resultados.apply(lambda x: x["Apuesta"] if x["Resultado"] == "PERDIÓ" else 0, axis=1)
    df_resultados["Ganado Acumulado"] = df_resultados["Ganado"].cumsum()
    df_resultados["Perdido Acumulado"] = df_resultados["Perdido"].cumsum()

    # Graficar
    plt.figure(figsize=(10,6))
    plt.plot(df_resultados["Ronda"], df_resultados["Ganado Acumulado"], label="Ganancias Acumuladas", color="green")
    plt.plot(df_resultados["Ronda"], df_resultados["Perdido Acumulado"], label="Pérdidas Acumuladas", color="red")
    plt.title(f"Evolución de Ganancias vs Pérdidas - {estrategia}")
    plt.xlabel("Número de Ronda")
    plt.ylabel("Dinero Acumulado ($)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def porcentaje_rondas_ganadas(historial_rondas, tiros_por_ronda):
    """
    Grafica el porcentaje de rondas en las que se ganó más tiros de los que se perdió.
    
    historial_rondas: lista de tuplas [(nro_ronda, cantidad_ganadas), ...]
    tiros_por_ronda: cantidad de tiros por cada ronda (asumimos que es constante)
    """

    # Procesamos las rondas
    resultados = []
    for ronda, ganadas in historial_rondas:
        perdidas = tiros_por_ronda - ganadas
        if ganadas > perdidas:
            resultados.append(1)  # Ganó más que perdió
        else:
            resultados.append(0)  # Perdió o empató

    total_rondas = len(resultados)
    rondas_ganadas = sum(resultados)
    porcentaje_ganadas = (rondas_ganadas / total_rondas) * 100

    # Gráfico de barras
    plt.figure(figsize=(8, 5))
    plt.bar(["Rondas con más victorias", "Rondas con más derrotas/empate"], 
            [rondas_ganadas, total_rondas - rondas_ganadas], 
            color=["green", "red"])
    plt.title("Porcentaje de rondas ganadas vs perdidas")
    plt.ylabel("Cantidad de Rondas")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()

    # Gráfico de torta
    plt.figure(figsize=(6,6))
    plt.pie(
        [rondas_ganadas, total_rondas - rondas_ganadas],
        labels=["Ganó más", "Perdió o empató"],
        autopct="%1.1f%%",
        startangle=140,
        colors=["green", "red"]
    )
    plt.title(f"Porcentaje de Rondas Ganadas")
    plt.tight_layout()
    plt.show()

    print(f"Ganaste más de lo que perdiste en el {porcentaje_ganadas:.2f}% de las rondas.")

    return porcentaje_ganadas


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
    return df_resultados


########################################################################################################################################################################################
def fibonacci(colores, balance, color_apuesta):
    i = 0
    multiplicador_de_apuesta = 1
    bet = apuesta * multiplicador_de_apuesta
    balance_inicial = balance
    salir = False
    for i in range(len(colores)):
        for j in range(len(colores[i])):
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
                    balance += bet
                    multiplicador_de_apuesta = aumentar_apuesta(
                        multiplicador_de_apuesta, True
                    )
                    bet = apuesta * multiplicador_de_apuesta  # Reducir apuesta
                else:
                    print("Perdió: $", bet)
                    balance -= bet
                    multiplicador_de_apuesta = aumentar_apuesta(
                        multiplicador_de_apuesta, False
                    )
                    bet = apuesta * multiplicador_de_apuesta  # Incrementar apuesta
            print("Saldo: $", balance)
        if salir:
            break

    if balance > 0:
        print("Dinero final: $", balance)
    else:
        print("Te has quedado sin dinero en la ronda ", i)


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

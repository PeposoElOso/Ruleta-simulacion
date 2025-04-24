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

def dalembert(colores, balance,color_apuesta):       
    bet = apuesta

    print(f"Balance inicial: {balance}")
    
    for i in range(len(colores)): 
        for j in range(len(colores[i])):
            
            if balance <= 0 or bet>balance:
                print("Saldo insuficiente.")
                salir= True
                break
            
            else :
                if colores[i][j] == color_apuesta:  
                    balance += bet
                    bet = max(apuesta, bet - apuesta)  # Reducir apuesta
                else:
                    balance -= bet
                    bet += apuesta  # Incrementar apuesta                                                                           
        if salir:
            break                 
    print(f"Balance final: {balance}")
            
    return balance

##############################################################################################################################################################################################


def velazquez(colores, balance,color_apuesta):
      
    bet = apuesta
    print(f"Balance inicial: {balance}")
    
    for i in range(len(colores)): 
        for j in range(len(colores[i])):
            
            if balance <= 0 or bet>balance:
                print("Saldo insuficiente.")
                salir= True
                break
            
            else :
                if colores[i][j] == color_apuesta:  
                    balance += bet
                    bet = max(apuesta, bet/2)  # divide apuesta
                else:
                    balance -= bet
                    bet += bet*2  # duplica apuesta
                                                                                
        if salir:
            break              
    print(f"Balance final: {balance}")           
  


 ########################################################################################################################################################################################


def martingala(colores,balance,color_apuesta, numeros):
    apuesta=10
    bet = apuesta
    historial = []
    contador = 0    
    
    print(f"Balance inicial: {balance}")
    
    for i in range(len(colores)): 
        for j in range(len(colores[i])):
            
            contador = contador + 1
            
            if balance <= 0 or bet>balance:
                print(f"Saldo insuficiente para continuar en la ronda {j}.")
                break

            if colores[i][j]  == color_apuesta:
                balance += bet
                historial.append((contador, numeros[i][j], colores[i][j] , bet, balance, 'GANÓ'))
                bet = apuesta  # Reinicia al monto base
            else:
                balance -= bet
                historial.append((contador, numeros[i][j], colores[i][j] , bet, balance, 'PERDIÓ'))
                bet *= 2  # Duplicar al perder

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



########################################################################################################################################################################################
def fibonacci(colores,balance, color_apuesta):
    i = 0
    bet = apuesta
    for i in range(len(colores)): 
        for j in range(len(colores[i])):
            
            if balance <= 0 or bet>balance:
                print("Saldo insuficiente.")
                salir= True
                break
            
            else :
                if colores[i][j] == color_apuesta:  
                    balance += bet
                    bet = aumentar_apuesta(apuesta, True)  # Reducir apuesta
                else:
                    balance -= bet
                    bet += aumentar_apuesta(apuesta, False)  # Incrementar apuesta
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

    idx = fib.index(valor_inicial)

    if retroceder:
        if idx < 2:
            return 1  # valor mínimo permitido
        return fib[idx - 2]
    else:
        while idx + 2 >= len(fib):
            fib.append(fib[-1] + fib[-2])
        return fib[idx + 2]


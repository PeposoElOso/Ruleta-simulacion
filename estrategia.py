import random
import funcs as f
import graf as gr



balance = 20  # Dinero inicial
apuesta = 10  # Apuesta base

def dalembert(colores, balance):
    
    color_apuesta= str(input("Ingrese el R o N "))
    
    if color_apuesta == "R" or color_apuesta == "r":
        color_apuesta = "rojo"
    elif color_apuesta == "N" or color_apuesta == "n":
        color_apuesta="negro"
    else:
        print("Color no válido. Debe ser 'R' o 'N'.")
        return
        
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



def velazquez(colores, balance):
    
    color_apuesta= str(input("Ingrese el R o N "))
    
    if color_apuesta == "R" or color_apuesta == "r":
        color_apuesta = "rojo"
    elif color_apuesta == "N" or color_apuesta == "n":
        color_apuesta="negro"
    else:
        print("Color no válido. Debe ser 'R' o 'N'.")
        return
        
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

            
    #return balance
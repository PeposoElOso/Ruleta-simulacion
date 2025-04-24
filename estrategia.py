rojo = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
negro = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


def fibonacci(dinero: float, numeros):
    rojo = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    negro = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    i = 0
    color = input("Ingrese a que color desea jugar: ")
    apuesta = 1
    if color == "R":
        while i < len(numeros[1]) and dinero > 0:
            if rojo.count(numeros[1][i]) == 1:
                dinero += apuesta
                apuesta = aumentar_apuesta(apuesta, True)
            else:
                dinero -= apuesta
                apuesta = aumentar_apuesta(apuesta, False)
            print(
                "Dinero: ",
                dinero,
                " en la tirada ",
                i,
                " de la ronda 1 con el numero: ",
                numeros[1][i],
            )
            i += 1
            if dinero <= 0:
                break
    elif color == "N":
        while i < len(numeros[1]) and dinero > 0:
            if negro.count(numeros[1][i]) == 1:
                dinero += apuesta
                apuesta = aumentar_apuesta(apuesta, True)
            else:
                dinero -= apuesta
                apuesta = aumentar_apuesta(apuesta, False)

            print(
                "Dinero:",
                dinero,
                " en la tirada ",
                i,
                "de la ronda 1 con el numero: ",
                numeros[1][i],
            )
            i += 1
            if dinero <= 0:
                break
    if dinero > 0:
        print("Dinero final: $", dinero)
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

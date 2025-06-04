from typing import Literal
import funcs as f
import graf as gr
import estrategia as e
import argparse

parser = argparse.ArgumentParser(
    prog="Ruleta",
    description="Calcular las estadisticas de la ruleta",
    epilog="Todos los parametros excepto el -e son obligatorios",
)

parser.add_argument(
    "-c", "--corridas", required=True, type=int, help="Cantidad de corridas"
)
parser.add_argument(
    "-n", "--tiradas", required=True, type=int, help="Cantidad de tiradas por corrida"
)
parser.add_argument(
    "-e",
    "--eleccion",
    type=int,
    help="Número elegido para apostar (0-36)",
)
parser.add_argument(
    "-s",
    "--estrategia",
    required=True,
    choices=["D", "V", "M", "F"],
    help="Estrategia a utilizar",
)
parser.add_argument(
    "-a",
    "--capital",
    required=True,
    choices=["i", "I", "A", "a"],
    help="Tipo de capital a utilizar infinito (i) o acotado (a)",
)
parser.add_argument(
    "-x",
    "--color",
    required=True,
    choices=["R", "r", "N", "n"],
    help="Color elegido: Rojo (r o R) Negro (n o N)",
)


args = parser.parse_args()
print(f"{args}")

numeros = f.ruleta(args.tiradas, args.corridas)  # tirodas / rondas
colores = f.color(numeros)

color_apuesta = args.color


if color_apuesta == "R" or color_apuesta == "r":
    color_apuesta = "rojo"
elif color_apuesta == "N" or color_apuesta == "n":
    color_apuesta = "negro"


balance_elegido = args.capital
balance = 0
if balance_elegido == "I" or balance_elegido == "i":
    balance = 99999999999999999999999999999999999999999999
elif balance_elegido == "A" or balance_elegido == "a":
    balance = int(input("Ingrese el saldo inicial: "))

estrategia = args.estrategia
if estrategia == "D" or estrategia == "d":
    e.dalembert(colores, balance, color_apuesta, numeros)
elif estrategia == "V" or estrategia == "v":
    e.velazquez(colores, balance, color_apuesta, numeros)
elif estrategia == "M" or estrategia == "m":
    e.martingala(colores, balance, color_apuesta, numeros)
elif estrategia == "F" or estrategia == "f":
    e.fibonacci(colores, balance, color_apuesta, numeros)
else:
    print("Color no válido. Debe ser 'R' o 'N'.")


# 1- grafico de tortas porcentaje de paridad
paridad = f.paridad(numeros)
gr.porcentaje_paridad(paridad[0], paridad[1])

# 4- comparacion de la desviacion estandar acumulada vs frecuencia de la apuesta
desvios = f.desviacion_acumulada(numeros)
medias = f.media_acumulada(numeros)
# 5- comparacion de la desviacion estandar acumulada vs media acumulada
gr.graficar_desvio_vs_media(desvios, medias)
# 6- comaracion de la frecuencia absoluta por numero
gr.graficar_frecuencia_absoluta_por_numero(f.frecuencia_absoluta_por_numero(numeros))
# 8-  compara las medias por cada ronda
medias_acumuladas = f.medias_acumuladas_por_ronda(numeros)
gr.graficar_medias_acumuladas_por_ronda(medias_acumuladas)

# 9- compara las desviaciones estandar por cada ronda
desviaciones = f.desviaciones_acumuladas_por_ronda(numeros)
gr.graficar_desviaciones_acumuladas_por_ronda(desviaciones)
if args.eleccion is not None:
    while True:
        try:
            apuesta = args.eleccion
            if 0 <= apuesta <= 36:
                break  # Salir del bucle si la entrada es válida
            else:
                print("Por favor, ingrese un número entre 0 y 36")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero")

    # 2- comparacion la frecuencia de la moda y la apuesta
    moda, acumulado, freq_moda, freq_apuesta = f.moda(numeros, apuesta)
    gr.graficar_moda_comparada(moda, apuesta, acumulado, freq_moda, freq_apuesta)

    # 3- comparacion de frecuencia relativa vs frecuencia esperada
    tiradas, freq_rel = f.frecuencia_relativa(numeros, apuesta)
    gr.graficar_frecuencia_relativa(apuesta, tiradas, freq_rel)

    frecuencias = f.frecuencia_absoluta_acumulada(numeros, apuesta)
    # gr.graficar_desviacion_vs_apuesta(desvios, frecuencias, apuesta)

    # 7- compara la frecuencia relativa de nuestra apuesta en cada ronda
    frecuencias_relativas = f.frecuencia_relativa_por_ronda(numeros, apuesta)
    gr.graficar_frecuencia_relativa_rondas(frecuencias_relativas, apuesta)

    # 10- compara la frecuencia de la apuesta por cada rondaS
    gr.graficar_frecuencias_acumuladas_por_ronda(
        f.frecuencia_absoluta_apuesta_por_ronda(numeros, apuesta)
    )
else:
    print("No se proporcionó un número para apostar. FIN DEL PROGRAMA")

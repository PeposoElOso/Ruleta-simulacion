import funcs as f
import graf as gr
import estrategia as e


color_apuesta= str(input("Ingrese el R o N "))
    
if color_apuesta == "R" or color_apuesta == "r":
    color_apuesta = "rojo"
elif color_apuesta == "N" or color_apuesta == "n":
    color_apuesta="negro"
else:
    print("Color no válido. Debe ser 'R' o 'N'.")


numeros =f.ruleta(5, 5)
colores = f.color(numeros)  
e.dalembert(colores, 100,color_apuesta, numeros)
#e.velazquez(colores,10000,color_apuesta,numeros)
#e.martingala(colores,100,color_apuesta,numeros)
#e.fibonacci(colores,100,color_apuesta)
apuesta= int(input("Ingrese el número que desea apostar (0-36): "))






# 1- grafico de tortas porcentaje de paridad
paridad = f.paridad(numeros)
gr.porcentaje_paridad(paridad[0], paridad[1])

# 2- comparacion la frecuencia de la moda y la apuesta
moda, acumulado, freq_moda, freq_apuesta = f.moda(numeros, apuesta)
gr.graficar_moda_comparada(moda, apuesta, acumulado, freq_moda, freq_apuesta)

# 3- comparacion de frecuencia relativa vs frecuencia esperada
tiradas, freq_rel = f.frecuencia_relativa(numeros, apuesta)
gr.graficar_frecuencia_relativa(apuesta, tiradas, freq_rel)

# 4- comparacion de la desviacion estandar acumulada vs frecuencia de la apuesta
desvios = f.desviacion_acumulada(numeros)
frecuencias = f.frecuencia_absoluta_acumulada(numeros, apuesta)
# gr.graficar_desviacion_vs_apuesta(desvios, frecuencias, apuesta)

# 5- comparacion de la desviacion estandar acumulada vs media acumulada
desvios = f.desviacion_acumulada(numeros)
medias = f.media_acumulada(numeros)
gr.graficar_desvio_vs_media(desvios, medias)

# 6- comaracion de la frecuencia absoluta por numero
gr.graficar_frecuencia_absoluta_por_numero(f.frecuencia_absoluta_por_numero(numeros))

# 7- compara la frecuencia relativa de nuestra apuesta en cada ronda
frecuencias_relativas = f.frecuencia_relativa_por_ronda(numeros, apuesta)
gr.graficar_frecuencia_relativa_rondas(frecuencias_relativas, apuesta)

# 8-  compara las medias por cada ronda
medias_acumuladas = f.medias_acumuladas_por_ronda(numeros)
gr.graficar_medias_acumuladas_por_ronda(medias_acumuladas)

# 9- compara las desviaciones estandar por cada ronda
desviaciones = f.desviaciones_acumuladas_por_ronda(numeros)
gr.graficar_desviaciones_acumuladas_por_ronda(desviaciones)

# 10- compara la frecuencia de la apuesta por cada rondaS
gr.graficar_frecuencias_acumuladas_por_ronda(
    f.frecuencia_absoluta_apuesta_por_ronda(numeros, apuesta)
)

# Implementa la estrategia Fibonacci
estrategia.fibonacci(50000, numeros)


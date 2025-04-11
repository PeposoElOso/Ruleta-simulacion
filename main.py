import funcs as f
import graf as gr

numeros =f.ruleta(10, 500)
apuesta=23

#grafico de tortas porcentaje de paridad
paridad = f.paridad(numeros)
gr.porcentaje_paridad( paridad[0], paridad[1])

#comparacion la frecuencia de la moda y la apuesta
moda, acumulado, freq_moda, freq_apuesta = f.moda(numeros, apuesta)
gr.graficar_moda_comparada(moda, apuesta, acumulado, freq_moda, freq_apuesta)

#comparacion de frecuencia relativa vs frecuencia esperada
tiradas, freq_rel = f.frecuencia_relativa(numeros, apuesta)
gr.graficar_frecuencia_relativa(apuesta, tiradas, freq_rel)

#comparacion de la desviacion estandar acumulada vs frecuencia de la apuesta
desvios = f.desviacion_acumulada(numeros)
frecuencias = f.frecuencia_absoluta_acumulada(numeros, apuesta)
gr.graficar_desviacion_vs_apuesta(desvios, frecuencias, apuesta)

#comparacion de la desviacion estandar acumulada vs media acumulada
desvios = f.desviacion_acumulada(numeros)
medias = f.media_acumulada(numeros)

gr.graficar_desvio_vs_media(desvios, medias)
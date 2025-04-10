import funcs as f
import graf as gr

numeros =f.ruleta(10, 5)
apuesta=23

Estad = f.estadisticas(numeros, apuesta)
print(Estad[4])
print("Estadisticas:")
print("Media:", f"{Estad[0]:.2f}")
print("Desviación estándar:", f"{Estad[1]:.2f}")
print("Frecuencia absoluta:", Estad[2])
print("Frecuencia relativa:", f"{Estad[3]:.2f}%")
print("Moda:", Estad[5])
print("Cantidad de números pares:", Estad[6])
print("Cantidad de números impares:", Estad[7])
print("Porcentaje de números impares:", f"{Estad[8]:.2f}%")
print("Porcentaje de números pares:", f"{Estad[9]:.2f}%")

gr.porcentaje_paridad( Estad[8], Estad[9])
gr.grafico_linea_moda_vs_apuesta(numeros, apuesta)
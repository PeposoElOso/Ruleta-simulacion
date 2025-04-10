import matplotlib.pyplot as plt
import funcs as f

def porcentaje_paridad(porcentaje_par, porcentaje_impar):
    
    # Pie chart (opcional) para mostrar proporción de pares vs impares
    plt.figure(figsize=(5, 5))
    plt.pie([porcentaje_par, porcentaje_impar], labels=['Pares', 'Impares'],
            autopct='%1.1f%%', colors=['#4CAF50', '#F44336'], startangle=90)
    plt.title('Proporción de Números Pares e Impares')
    plt.tight_layout()
    plt.show()


def grafico_linea_moda_vs_apuesta(numeros, apuesta):
    frec_moda = []
    frec_apuesta = []

    for ronda in numeros:
        moda, freq_moda = f.frecuencia_moda(ronda)
        freq_ap = f.frecuencia_absoluta(ronda, apuesta)
        frec_moda.append(freq_moda)
        frec_apuesta.append(freq_ap)

    plt.figure(figsize=(8, 5))
    plt.plot(frec_moda, label='Frecuencia Moda', marker='o')
    plt.plot(frec_apuesta, label=f'Frecuencia del {apuesta}', marker='x')
    plt.title('Frecuencia Moda vs Número Apostado')
    plt.xlabel('Ronda')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

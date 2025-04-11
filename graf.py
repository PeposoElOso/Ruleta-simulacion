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


def graficar_moda_comparada(moda, apuesta, acumulado, freq_moda, freq_apuesta):
    plt.figure(figsize=(10, 5))
    plt.plot(acumulado, freq_moda, label=f"Moda ({moda})", marker='o', color='blue')
    plt.plot(acumulado, freq_apuesta, label=f"Apuesta ({apuesta})", marker='x', color='orange')
    plt.title("Frecuencia acumulada: Moda vs Apuesta")
    plt.xlabel("Cantidad de tiradas")
    plt.ylabel("Frecuencia acumulada")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def graficar_frecuencia_relativa(apuesta, tiradas, frecuencia_relativa):
    plt.figure(figsize=(10, 5))
    plt.plot(tiradas, frecuencia_relativa, label=f'Frecuencia relativa del número {apuesta}', color='blue')
    plt.axhline(y=100/37, color='red', linestyle='--', label='Frecuencia esperada (2.70%)')

    plt.title('Comparación de frecuencia relativa vs frecuencia esperada')
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Frecuencia relativa (%)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def graficar_desviacion_vs_apuesta(desvios, frecuencias, apuesta):
    tiradas = list(range(1, len(desvios) + 1))

    plt.figure(figsize=(10, 6))
    plt.plot(tiradas, desvios, label='Desviación estándar acumulada', color='orange')
    plt.plot(tiradas, frecuencias, label=f'Frecuencia de aparición del número {apuesta}', color='green')

    plt.title('Desviación estándar vs Frecuencia de la apuesta')
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Valor')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

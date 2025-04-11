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
    plt.plot(acumulado, freq_moda, label=f"Moda ({moda})", color='blue')
    plt.plot(acumulado, freq_apuesta, label=f"Apuesta ({apuesta})", color='orange')
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


def graficar_desvio_vs_media(desvios, medias):
    tiradas = list(range(1, len(desvios) + 1))
    
    
    plt.figure(figsize=(10, 6))
    plt.plot(tiradas, desvios, label='Desviación estándar acumulada', color='red')
    plt.plot(tiradas, medias, label='Media acumulada', color='blue')
    plt.axhline(18, color='gray', linestyle='--', label='Media esperada')
    plt.title('Desviación estándar vs Media a lo largo de las tiradas')
    plt.xlabel('Cantidad de tiradas')
    plt.ylabel('Valor')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def graficar_frecuencia_absoluta_por_numero(frecuencia_df):
    plt.figure(figsize=(10, 6))
    
    # Gráfico de barras
    plt.bar(frecuencia_df['Número'], frecuencia_df['Frecuencia'], color='skyblue', label='Frecuencia Absoluta')
    
    # Línea que sigue las subidas y bajadas
    plt.plot(frecuencia_df['Número'], frecuencia_df['Frecuencia'], color='darkblue', marker='o', linestyle='-', linewidth=2, label='Tendencia')

    plt.title('Frecuencia Absoluta por Número')
    plt.xlabel('Número')
    plt.ylabel('Frecuencia')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.legend()
    plt.tight_layout()
    plt.show()

    
def graficar_frecuencia_relativa_rondas(frecuencias_relativas, apuesta):
    plt.figure(figsize=(10, 6))

    for i, ronda in enumerate(frecuencias_relativas):
        plt.plot(range(1, len(ronda) + 1), ronda, label=f'Ronda {i + 1}')

    plt.axhline(100/37, color='gray', linestyle='--', label='Esperado (2.70%)')
    plt.title(f'Frecuencia relativa acumulada del número {apuesta}')
    plt.xlabel('Tirada')
    plt.ylabel('Frecuencia relativa (%)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    
def graficar_medias_acumuladas_por_ronda(medias_acumuladas):
    plt.figure(figsize=(10, 6))
    
    for i, medias in enumerate(medias_acumuladas):
        plt.plot(range(1, len(medias)+1), medias, label=f'Ronda {i+1}')
    
    plt.axhline(18, color='gray', linestyle='--', label='Media esperada (18.0)')
    plt.title('Evolución de la Media Acumulada por Ronda')
    plt.xlabel('Tirada dentro de la ronda')
    plt.ylabel('Media acumulada')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def graficar_desviaciones_acumuladas_por_ronda(desviaciones_acumuladas):
    plt.figure(figsize=(10, 6))
    
    for i, desvios in enumerate(desviaciones_acumuladas):
        plt.plot(range(1, len(desvios)+1), desvios,  label=f'Ronda {i+1}')
    
    plt.title('Evolución del Desvío Estándar Acumulado por Ronda')
    plt.xlabel('Tirada dentro de la ronda')
    plt.ylabel('Desvío estándar acumulado')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def graficar_frecuencias_acumuladas_por_ronda(frecuencias_acumuladas):
    plt.figure(figsize=(10, 6))
    for i, frecuencias in enumerate(frecuencias_acumuladas):
        plt.plot(frecuencias, linewidth=2)

    plt.title('Frecuencia Acumulada por Ronda')
    plt.xlabel('Tirada dentro de la ronda')
    plt.ylabel('Frecuencia acumulada')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

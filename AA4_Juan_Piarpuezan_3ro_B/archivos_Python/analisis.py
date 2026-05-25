import cProfile
import pstats
import matplotlib.pyplot as plt
import numpy as np
import math

def run_primos_opt():
    def es_primo_opt(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    return [num for num in range(2, 100001) if es_primo_opt(num)]

# Profiling
cProfile.run('run_primos_opt()', 'IMAGENES/perfil.stats')

with open('IMAGENES/profiling_optimizado.txt', 'w', encoding='utf-8') as f:
    stats = pstats.Stats('IMAGENES/perfil.stats', stream=f)
    stats.sort_stats('cumulative')
    stats.print_stats(10)

# Gráficos (REEMPLAZA estos valores con tus tiempos reales)
tiempos = {
    'Original': 14.8545,
    'Optimizado': 0.5000
}
mejora = ((tiempos['Original'] - tiempos['Optimizado']) / tiempos['Original']) * 100

# Gráfico 1: Comparativa
plt.figure(figsize=(8, 5))
plt.bar(tiempos.keys(), tiempos.values(), color=['#e74c3c', '#2ecc71'])
plt.ylabel('Tiempo (segundos)')
plt.title('Comparativa: Codigo Original vs Optimizado')
plt.grid(axis='y', alpha=0.3)
plt.savefig('IMAGENES/comparativa_tiempos.png', dpi=300, bbox_inches='tight')

# Gráfico 2: Mejora
plt.figure(figsize=(6, 6))
plt.pie([mejora, 100 - mejora], 
        labels=[f'Mejora: {mejora:.1f}%', 'Tiempo restante'],
        colors=['#2ecc71', '#bdc3c7'], 
        startangle=90)
plt.title('Reduccion de tiempo de ejecucion')
plt.savefig('IMAGENES/distribucion_mejora.png', dpi=300, bbox_inches='tight')

print("Archivos generados: profiling_optimizado.txt, comparativa_tiempos.png, distribucion_mejora.png")

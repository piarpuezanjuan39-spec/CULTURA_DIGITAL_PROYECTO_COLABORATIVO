# codigo_optimizado.py
import time
import math
import numpy as np

def es_primo_opt(n):
    """Version optimizada: solo verifica hasta raiz cuadrada y salta pares"""
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

def encontrar_primos_opt(rango_max):
    """Usa list comprehension + NumPy para mayor eficiencia"""
    primos = [num for num in range(2, rango_max + 1) if es_primo_opt(num)]
    return np.array(primos)

# Medición de tiempo
inicio = time.time()
resultado = encontrar_primos_opt(100000)
fin = time.time()

print(f"Números primos encontrados: {len(resultado)}")
print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
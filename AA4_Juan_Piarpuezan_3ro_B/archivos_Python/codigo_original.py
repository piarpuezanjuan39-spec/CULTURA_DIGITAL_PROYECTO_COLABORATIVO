# codigo_original.py
import time

def es_primo(n):
    """Verifica si un número es primo (versión básica - ineficiente)"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def encontrar_primos(rango_max):
    """Encuentra todos los primos hasta rango_max"""
    primos = []
    for num in range(1, rango_max + 1):
        if es_primo(num):
            primos.append(num)
    return primos

# Medición de tiempo
inicio = time.time()
resultado = encontrar_primos(100000)
fin = time.time()

print(f"Números primos encontrados: {len(resultado)}")
print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")

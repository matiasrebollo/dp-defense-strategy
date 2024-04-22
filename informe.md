# Objetivo

El objetivo del presente trabajo es idear un algoritmo que indique la estrategia de defensa optima para defender Ba Sing Se del ataque de la nación del fuego. Dicho algoritmo debe implementarse mediante programación dinámica. Además, se brindará un análisis completo del problema y del algoritmo en cuestión.

# Análisis del Problema

### Ecuación de Recurrencia

$$
OPT(n) = \max_{0\le k\lt n}\left(OPT(n-k) +\min(x_{n},f(n-k))\right)
$$

# Algoritmo y Complejidad
A continuación expondremos el código de nuestro algoritmo junto con el respectivo análisis de complejidad.

## Implementación

```python
# Código en main.py

def obtener_optimo(ataques, potencias):
    n = len(ataques)
    optimo = [0]*(n+1)
    for i in range(1, len(optimo)):
        optimo[i] = max(map(lambda x, c: x + min(ataques[i-1],potencias[i-c-1]), optimo[:i], range(i))) 
    return optimo


def construir_estrategia(ataques, potencias, optimo):
    solucion = []
    i = len(optimo)-1
    while i > 0:
        solucion.append(i)
        anteriores = list(map(lambda x, c: x + min(ataques[i-1],potencias[i-c-1]), optimo[:i], range(i)))
        i = anteriores.index(optimo[i])
    return list(reversed(solucion))

```

## Análisis Complejidad
Complejidad Final: $\mathcal{O}(n²)$

# Análisis variabilidad de valores


# Mediciones

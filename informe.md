# Objetivo

El objetivo del presente trabajo es idear un algoritmo que indique la estrategia de defensa óptima para defender Ba Sing Se del ataque de la Nación del Fuego. Dicho algoritmo debe implementarse mediante programación dinámica. Además, se brindará un análisis completo del problema y del algoritmo en cuestión.

# Análisis del Problema

Para un período de $n$ minutos, se consta de dos conjuntos de datos:
- $x_i$: la cantidad de enemigos que llegarán en el minuto $i$.
- $f(i)$: la potencia del ataque de los Dai Li habiendo pasado $i$ minutos desde el último ataque.

Nuestro objetivo es decidir cuáles son los minutos cruciales para atacar a los enemigos y así maximizar sus bajas.

Como se pide una solución mediante programación dinámica, pensemos en los casos bases:
- $n=0$: No hay ataque, no hay bajas enemigas.
- $n=1$: Al ser la única oportunidad de ataque, se realiza el mismo, provocando $\min(x_1, f(1))$ bajas enemigas.

Sigamos con el análisis de casos sencillos:
- $n=2$: Como **no tiene sentido no atacar en el último minuto**, las posibles estrategias son atacar en ambos minutos (Atacar, Atacar) o cargar el ataque por un minuto y atacar en el último (Cargar, Atacar). Elegiremos aquella que cause mayor daño al enemigo, o en otras palabras:
$$\max(\min(x_1,f(1))+\min(x_2, f(1)), \min(x_2, f(2)))$$

- $n=3$: Tenemos el doble de estrategias que el caso anterior:
    - **Atacar**, **Atacar**, Atacar
    - **Cargar**, **Atacar**, Atacar
    - Atacar, Cargar, Atacar
    - Cargar, Cargar, Atacar

Si observamos bien, las primeras dos estrategias tienen como subproblema el del punto anterior.

### Ecuación de Recurrencia

$$
OPT(n) = \max_{0\le k\lt n}\left(OPT(k) +\min(x_{n},f(n-k))\right)
$$

# Algoritmo y Complejidad
A continuación expondremos el código de nuestro algoritmo junto con el respectivo análisis de complejidad.

## Implementación

```python
# Código en main.py

def obtener_optimo(ataques, potencias):
    n = len(ataques)
    optimos = [0]*(n+1)
    for i in range(1, len(optimos)):
        optimos[i] = max(map(lambda opt, k: opt + min(ataques[i-1],potencias[i-1-k]), optimos[:i], range(i))) 
    return optimos


def construir_estrategia(ataques, potencias, optimos):
    solucion = []
    i = len(optimos)-1
    while i > 0:
        solucion.append(i)
        anteriores = list(map(lambda opt, k: opt + min(ataques[i-1],potencias[i-1-k]), optimos[:i], range(i)))
        i = anteriores.index(optimos[i])
    return list(reversed(solucion))

```

## Análisis Complejidad
Complejidad final: $\mathcal{O}(n²)$

# Análisis variabilidad de valores


# Mediciones

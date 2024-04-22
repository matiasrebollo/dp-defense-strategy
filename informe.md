# Objetivo

El objetivo del presente trabajo es idear un algoritmo que indique la estrategia de defensa optima para defender Ba Sing Se del ataque de la nación del fuego. Dicho algoritmo debe implementarse mediante programación dinámica. Además, se brindará un análisis completo del problema y del algoritmo en cuestión.

# Análisis del Problema

Para un periodo de $n$ minutos, se consta de dos conjuntos de datos:
- $x_i$ la cantidad de enemigos que llegaran en el minuto $i$.
- $f(i)$ la potencia del ataque de los Dai Li habiendo pasado $i$ minutos desde el ultimo ataque.

Nuestro objetivo es decidir cuales son los minutos cruciales para atacar a los enemigos y así maximizar sus bajas.

Como se pide una solucion mediante programacion dinamica, pensemos en los casos bases:
- $n=0$: No hay ataque, no hay bajas enemigas.
- $n=1$: Al ser la unica oportunidad de ataque, hay que atacar a los enemigos, provocando $\min(x_1, f(1))$ bajas enemigas.

Sigamos con el análisis de casos sencillos.
- $n=2$: Como **no tiene sentido no atacar en el ultimo minuto**, las posibles estrategias son atacar en ambos minutos (Ataque, Ataque), cargar el ataque por un minuto y atacar en el ultimo minuto (Cargar, Ataque). Eligiremos aquella que cause mayor daño al enemigo, o en otras palabras $\max(\min(x_2, f(2)), \min(x_1,f(1)+\min(x_1, f(1)))$.
- $n=3$: Tenemos el doble de estrategias que el caso anterior:
    - **Atacar**, **Atacar**, Atacar
    - **Cargar**, **Atacar**, Atacar
    - Atacar, Cargar, Atacar
    - Cargar, Cargar, Atacar

  Si observamos bien, las primeras dos estrategias, tienen parte del problema del punto anterior

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

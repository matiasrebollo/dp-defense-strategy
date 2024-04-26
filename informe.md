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

Si observamos bien, las primeras dos estrategias tienen como subproblema el del punto anterior, y como una vez se ataca se reinicia la carga del ataque sin importar todo lo que vino antes, entre estas dos opciones debemos elegir la que mas enemigos haya derrotado, y este paso ya lo hemos calculado en el paso anterior, con n=2.

El problema no acaba ahi, pues puede ser que la estrategia correcta este entre la últimas dos, las cuales de manera similar a lo dicho recientemente,  incluyen un subproblema anterior, en este caso para n=1 y n=0, y en cada caso hay que tener en cuenta que la carga ira creciendo, pues es una funcion monotona creciente.
Para resumir, podemos escribir la ecuacion:

$$\max(OPT(0) + \min(x_3,f(3)), OPT(1) + \min(x_3, f(2)), OPT(2) + \min(x_3, f(1)))$$

Aplicando la ecucion para cualquier minuto $n$, obtenemos la ecuacion de recurrencia:

### Ecuación de Recurrencia

$$
OPT(n) = \max_{0\le k\lt n}\left(OPT(k) +\min(x_{n},f(n-k))\right)
$$

Entonces proponemos el siguiente algoritmo:
1. Para cada minuto $i$ calculo la mayor cantidad de enemigos derrotados aplicando la ecuacion de recurrencia.
2. Para construir la estrategia empiezo desde el ultimo optimo calculado, agrego su respectivo minuto a la solucion, y mediante la ecuacion de recurrencia obtengo la cantidad de enemigos derrotados para cada minuto anterior, luego busco el optimo actual en esta lista (obtengo su indice) y repito todo desde ese minuto hasta llegar al inicio.  

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
El algoritmo consta de dos partes: 
1. Obtener los optimos para cada subproblema: Para eso se iterara por cada oleada de enemigos (un total de $n$ veces) y para cada iteracion aplicaremos la ecuacion de recurrenciapara obtener el optimo actual, iterando por las soluciones a los subproblemas ya calculados. Esto ultimo puede acotarse a $\mathcal{O}(n)$. Luego la complejidad temporal de esta parte queda en $n\mathcal{O}(n) = \mathcal{O}(n²) $.
2. Reconstruir la estrategia optima a partir del arreglo de optimos: partiendo desde el ultimo minuto, buscamos el optimo actual entre las propuestas de los subproblemas anteriores en $\mathcal{O}(n)$ y repetimos lo anterior desde el resultado de la busqueda. En el peor de los casos atacamos en todos los minutos, por lo que la complejidad queda como $n\mathcal{O}(n) = \mathcal{O}(n²) $

Complejidad final: $\mathcal{O}(n²) + \mathcal{O}(n²) = \mathcal{O}(n²)$ en funcion del tamaño del arreglo de entrada.

# Análisis variabilidad de valores


# Mediciones

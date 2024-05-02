# Objetivo

El objetivo del presente trabajo es idear un algoritmo que indique la estrategia de defensa óptima para defender Ba Sing Se del ataque de la Nación del Fuego. Dicho algoritmo debe implementarse mediante programación dinámica. Además, se brindará un análisis completo del problema y del algoritmo en cuestión.

# Análisis del Problema

Primero definimos las variables de nuestro problema:
- $n$ la duracion (en minutos) del ataque enemigo.
- $x_i$: la cantidad de enemigos que llegarán en el minuto $i$.
- $f(i)$: la potencia del ataque de los Dai Li, tras ser cargado por $i$ minutos.

Además, se debe tener en cuenta lo siguiente:
- Si se decide atacar a los enemigos en el minuto $k$, habiendo pasado $i$ minutos desde el ultimo ataque, el total de bajas enemigas será de $\min(x_i, f(i))$
- Luego de atacar, se pierde la carga acumulada.

Nuestra tarea es decidir cuáles son los minutos cruciales para atacar a los enemigos y así maximizar sus bajas.

### Análisis casos bases

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

    Si observamos bien, las primeras dos estrategias tienen como subproblema el del punto anterior, y como una vez se ataca se reinicia la carga del ataque sin importar todo lo que vino antes, entre estas dos opciones debemos elegir la que mas enemigos haya derrotado, y este paso ya lo hemos calculado en el paso anterior, con $n=2$.

    El problema no acaba ahi, pues puede ser que la estrategia correcta este entre la últimas dos, las cuales de manera similar a lo dicho recientemente,  incluyen un subproblema anterior, en este caso para n=1 y n=0, y en cada caso hay que tener en cuenta que la carga ira creciendo, pues es una funcion monotona creciente.
Para resumir, podemos escribir la ecuacion:

$$\max(OPT(0) + \min(x_3,f(3)), OPT(1) + \min(x_3, f(2)), OPT(2) + \min(x_3, f(1)))$$

Aplicando la ecucion para cualquier minuto $n$, obtenemos la ecuacion de recurrencia:

#### Ecuación de Recurrencia

$$
OPT(n) = \max_{0\le k\lt n}\left(OPT(k) +\min(x_{n},f(n-k))\right)
$$

### Algoritmo Propuesto

Proponemos el siguiente algoritmo:
1. **Obtengo los optimos para cada subproblema**:
    + Itero por cada minuto $i$.
    + Por cada iteración calculo el optimo mediante la ecuacion de recurrencia.

2. **Construir la estrategia**:
    + Empiezo desde el ultimo optimo calculado.
    + Agrego su respectivo minuto a la solucion.
    + Busco cuál fue el minuto donde se ataco para llegar al óptimo.
    + A partir de este minuto, repito los pasos anteriores hasta llegar al minuto 0.
  

# Algoritmo y Complejidad
A continuación expondremos el código de nuestro algoritmo junto con el respectivo análisis de complejidad.

## Implementación

```python
# Código en main.py

def obtener_optimo(enemigos, potencias):
    n = len(enemigos)
    optimos = [0]*(n+1)
    for i in range(1, n + 1):
        maximo = 0

        for k in range(i):
            valor_actual = optimos[k] + min(enemigos[i - 1], potencias[i - 1 - k])
            maximo = max(valor_actual, maximo)
        optimos[i] = maximo

    return optimos


def construir_estrategia(enemigos, potencias, optimos):
    def construir_estrategia(enemigos, potencias, optimos):
    solucion = []
    i = len(enemigos)
    while i > 0:
        solucion.append(i)

        for k in range(i):
            valor = optimos[k] + min(enemigos[i - 1], potencias[i - 1 - k])
            if valor == optimos[i]:
                i = k
                break    

    solucion.reverse()
    return solucion
```

## Análisis Complejidad Temporal
El algoritmo consta de dos partes: 

1. **Obtener los optimos para cada subproblema**: 
    + Iterar por cada minuto $i$ (un total de $n$ veces). 
    + En cada iteracion aplicar la ecuacion de recurrencia, iterando por las soluciones de los $k$ subproblemas ya calculados. $\mathcal{O}(k)$
    
    Como $k \le n$, la complejidad temporal de esta parte queda en $n\cdot \mathcal{O}(k) = n\cdot\mathcal{O}(n) =\mathcal{O}(n²) $.


2. **Reconstruir la estrategia optima a partir del arreglo de optimos**:
    + Buscar el óptimo actual entre las propuestas de los subproblemas anteriores: $\mathcal{O}(n)$ 
    + Repetir lo anterior desde el resultado de la busqueda, hasta llegar al inicio ($m$ veces para una solucion de $m$ ataques).

    Como $m\le n$, la complejidad queda como $m\cdot\mathcal{O}(n) = n\cdot\mathcal{O}(n) = \mathcal{O}(n²) $

Complejidad final: $\mathcal{O}(n²) + \mathcal{O}(n²) = \mathcal{O}(n²)$ en funcion del tamaño del arreglo de entrada.

# Análisis variabilidad de valores

Se detectó un caso particular

### Ataque con carga minima limpia cualquier oleada de enemigos

En otras palabras, $f(1) > x_i \forall i$. Estamos en un caso donde la diferencia entre cargar el ataque o no es nula, pues al final terminan eliminando la misma cantidad de enemigos. Por ende, la mejor opción siempre será _atacar en todos los turnos_, y la _cantidad total de bajas enemigas será equivalente al total de enemigo_.

No afecta la complejidad, debido a que la primer parte de nuestro algoritmo no logra salvarse de iterar por cada posible óptimo para cada minuto (al menos en nuestra impementación). 
Cabe mencionar que, si bien no afecta la complejidad total, al atacar en todos los minutos, terminaremos en el peor caso de la reconstruccion de la solución al tener que realizar operaciones lineales para cada minuto.

Tampoco es una situación que afecte la optimalidad de nuestro algoritmo, pues al tratarse de un algoritmo por programación dinámica, este _explora de manera implícita el espacio de posibilidades_, por lo que al final eligirá las opciones que más le sirvan, y sabrá detectar con facilidad que atacar varias veces con el mismo impacto será mejor que cargar el ataque y conseguir un resultado menor. 

# Casos de Prueba

Se realizaron varios ejemplos de ejecución para validar la eficacia y optimalidad del algoritmo implementado. Además de los proporcionados por la cátedra, se incluyeron casos adicionales para verificar la cobertura y robustez del algoritmo. Estos se encuentran en la carpeta 'ejemplos' del repositorio.

Los casos de prueba abarcan diversas situaciones para identificar posibles fallos y asegurar el funcionamiento del algoritmo en escenarios no contemplados inicialmente. Entre los ejemplos de ejecución se encuentran:

- **Vector vacío**: para asegurar que el algoritmo maneje correctamente situaciones sin enemigos.

- **Un solo valor**: para asegurar que el algoritmo ataque ante una sola tropa de enemigos.

- **Dos valores**: para asegurar que el algoritmo elija la mejor opción entre cargar y atacar o atacar y atacar, ante dos tropas de enemigos.

- **Patrones de enemigos**: entre ellos se incluyen cantidades de enemigos crecientes, decrecientes, constantes y variaciones extremas. Estos casos aseguran que el algoritmo maneje correctamente estas situaciones y elija sabiamente cuándo atacar y cuándo cargar.

- **Valores muy grandes**: para probar la resistencia del algoritmo ante valores altos y detectar posibles problemas de precisión.

El algoritmo respondió satisfactoriamente a todos estos casos, demostrando su eficacia y capacidad de adaptarse a una amplia gama de situaciones. Esto indica que el algoritmo es óptimo en todos los escenarios evaluados.


# Mediciones

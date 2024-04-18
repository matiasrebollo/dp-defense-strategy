# Trabajo Práctico 2: Programación Dinámica para el Reino de la Tierra

El presente trabajo busca evaluar el desarrollo y análisis de un algoritmo de Programación Dinámica. La fecha de entrega del mismo es el 6/05.
Introducción

Es el año 80 DG. Ba Sing Se es una gran ciudad del Reino de la Tierra. Allí tiene lugar el palacio Real. Por esto, se trata de una ciudad fortificada, que ha logrado soportar durante más de 110 años los ataques de la Nación del Fuego. Los Dai Li (policía secreta de la ciudad) la defienden utilizando técnicas de artes marciales, Tierra-control, y algunos algoritmos. Nosotros somos los jefes estratégicos de los Dai Li.

Gracias a las técnicas de Tierra-control, lograron detectar que la Nación del Fuego planea un ataque ráfaga con miles de soldados maestros Fuego. El ataque sería de la siguiente forma:

Ráfagas de soldados llegarían durante el transcurso de nn minutos. En el ii-ésimo minuto llegarán xixi​ soldados. Gracias a las mediciones sísmicas hechas con sus técnicas, los Dai Li lograron obtener los valores de x1,x2,⋯ ,xn.

Cuando los integrantes del equipo juntan sus fuerzas, pueden generar fisuras que permiten destruir parte de las armadas enemigas. La fuerza de este ataque depende cuánto tiempo se utilizó para cargar energía. Más específicamente, podemos decir que hay una función f(⋅) que indica que si transcurrieron j minutos desde que se utilizó este ataque, entonces es capaz de eliminar hasta f(j) soldados enemigos.

Si se utiliza este ataque en el k-ésimo minuto, y transcurrieron j minutos desde su último uso, entonces se eliminará a min⁡(xk,f(j)) soldados (y luego de su uso, se utilizó toda la energía que se había acumulado).

Inicialmente los Dai Li comienzan sin energía acumulada.

La función de recarga será una función monótona creciente.

Como jefes estratégicos de los Dai Li, es nuestro deber determinar en qué momentos debemos realizar estos ataques de fisuras para eliminar a tantos enemigos en total como sea posible.

Consigna

Hacer un análisis del problema, plantear la ecuación de recurrencia correspondiente y proponer un algoritmo por programación dinámica que obtenga la solución óptima al problema planteado: Dada la secuencia de de llegadas de enemigos x1,x2,⋯ ,xn y la función de recarga f(⋅) (dada por una tabla, con lo cual puede considerarse directamente como una secuencia de valores), determinar la cantidad máxima de enemigos que se pueden atacar, y en qué momentos se harían los correspondientes ataques.

Escribir el algoritmo planteado. Describir y justificar la complejidad de dicho algoritmo. Analizar si (y cómo) afecta a los tiempos del algoritmo planteado la variabilidad de los valores de las llegadas de enemigos y recargas.

Analizar si (y cómo) afecta a la optimalidad del algoritmo planteado la variabilidad de los valores de las llegadas de enemigos y recargas

Realizar ejemplos de ejecución para encontrar soluciones y corroborar lo encontrado. Adicionalmente, el curso proveerá con algunos casos particulares que deben cumplirse su optimalidad también.

De las pruebas anteriores, hacer también mediciones de tiempos para corroborar la complejidad teórica indicada. Realizar gráficos correspondientes. Generar todo set de datos necesarios para estas pruebas.

Agregar cualquier conclusión que parezca relevante.


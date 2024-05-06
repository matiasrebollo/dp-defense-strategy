import matplotlib.pyplot as plt
from time import perf_counter
from random import uniform
from main import obtener_optimos, construir_estrategia
from utils import MAX_ENEMIGOS, MAXIMO_PODER, TAM_MUESTRA

plt.clf()
tamanios_datos = [x for x in range(10, 5000, 100)]
tiempos_caso_1 = []
tiempos_caso_2 = []

for n in tamanios_datos:
    enemigos = [1 for _ in range(n)]
    potencias = [uniform(2, MAXIMO_PODER) for _ in range(n)]
    tiempo_acumulado = 0
    for _ in range(TAM_MUESTRA):
        inicio = perf_counter()
        optimos = obtener_optimos(enemigos, potencias)
        construir_estrategia(enemigos, potencias, optimos)
        fin = perf_counter()
        tiempo_ms = (fin - inicio)*1000
        tiempo_acumulado += tiempo_ms
    tiempos_caso_1.append(tiempo_acumulado/TAM_MUESTRA)

for n in tamanios_datos:
    enemigos = [1 for _ in range(n)]
    enemigos[n-1] = MAX_ENEMIGOS
    potencias = [1 for _ in range(n)]
    potencias[n-1] = MAXIMO_PODER
    tiempo_acumulado = 0
    for _ in range(TAM_MUESTRA):
        inicio = perf_counter()
        optimos = obtener_optimos(enemigos, potencias)
        construir_estrategia(enemigos, potencias, optimos)
        fin = perf_counter()
        tiempo_ms = (fin - inicio)*1000
        tiempo_acumulado += tiempo_ms
    tiempos_caso_2.append(tiempo_acumulado/TAM_MUESTRA)

plt.title("Análisis de variabilidad")
plt.xlabel("cantidad de minutos")
plt.ylabel("tiempo consumido [ms]")
plt.plot(tamanios_datos, tiempos_caso_1, label='Ataques todos los minutos')
plt.plot(tamanios_datos, tiempos_caso_2, label='Ataque último minuto')
plt.legend()
plt.savefig("img/grafico_variabilidad.png")
plt.show()
from time import perf_counter
from utils import obtener_funcion_potencias_random
from random import randrange
from scipy.optimize import curve_fit
from main import obtener_optimos, construir_estrategia
import matplotlib.pyplot as plt
import numpy as np

TAM_MUESTRA = 5 # Numeros mas grandes tardaban demasiado
MAX_ENEMIGOS = 1000000 # Numero muy grande, para que funcione randrange

def ajuste(x, a, b, c):
    return a*x**2 + b*x + c


def obtener_tiempo(n):
    enemigos_arr = [randrange(1, 1000000) for _ in range(n)]
    potencia_ataques = obtener_funcion_potencias_random(n)

    tiempo_acumulado = 0

    for _ in range(TAM_MUESTRA):
        start = perf_counter()
        optimos = obtener_optimos(enemigos_arr, potencia_ataques)
        construir_estrategia(enemigos_arr, potencia_ataques, optimos)
        fin = perf_counter()
        tiempo_ms = (fin - start)*1000
        tiempo_acumulado += tiempo_ms

    return tiempo_acumulado/TAM_MUESTRA


tamanio_datos = np.arange(10, 5000, 100)
fun = np.frompyfunc(obtener_tiempo, 1, 1)
tiempos_ejecucion = fun(tamanio_datos)
popt, _ = curve_fit(ajuste, tamanio_datos, tiempos_ejecucion)

figure, axis = plt.subplots(2, 1)

axis[0].plot(tamanio_datos, tiempos_ejecucion)
axis[0].set_title("Tiempo de ejecución en función del tamaño del arreglo")
axis[0].set_xlabel("cantidad de minutos")
axis[0].set_ylabel("tiempo consumido [ms]")

axis[1].plot(tamanio_datos, ajuste(tamanio_datos, *popt))
axis[1].set_title("Complejidad esperada")
axis[1].set_xlabel("cantidad de minutos")
axis[1].set_ylabel("tiempo consumido [ms]")

plt.tight_layout()
plt.savefig("img/grafico_complejidad.png")
plt.show()
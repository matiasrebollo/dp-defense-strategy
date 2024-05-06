from random import randrange

TAM_MUESTRA = 5 # Numeros mas grandes tardaban demasiado
MAX_ENEMIGOS = 1000000 # Numero muy grande, para que funcione randrange
MAXIMO_PODER = 1000000 # Para que funcione randrange

def calcular_tropas_eliminadas(enemigos, potencias, estrategia):
    cant_tropas = 0
    potencia = 1
    for i in range(1, len(enemigos)+1):
        if i in estrategia:
            cant_tropas += min(enemigos[i-1], potencias[potencia-1])
            potencia = 1
        else: 
            potencia += 1

    return cant_tropas

def obtener_optimo_bt(enemigos, potencias, optimo_pd, i, optimo_actual, ultimo_ataque):
    if i == len(enemigos):
        return optimo_actual
    
    if optimo_actual + sum(enemigos[i:]) <= optimo_pd:
        return optimo_pd
    
    nuevo_optimo = optimo_actual + min(enemigos[i], potencias[i-ultimo_ataque])
    optimo_atacando = obtener_optimo_bt(enemigos, potencias, optimo_pd, i+1, nuevo_optimo, i+1)
    optimo_sin_atacar = obtener_optimo_bt(enemigos, potencias, optimo_pd, i+1, optimo_actual, ultimo_ataque)
    
    return max(optimo_atacando, optimo_sin_atacar)

def obtener_funcion_potencias_random(n):
    potencias = [0]*n
    for i in range(n):
        if i == 0:
            potencias[i] = randrange(0, MAXIMO_PODER)
        else:
            potencias[i] = randrange(potencias[i-1], MAXIMO_PODER)
    return potencias
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

def verificar_optimalidad(enemigos, potencias, optimo_pd):
    return optimo_pd == obtener_optimo_bt(enemigos, potencias, optimo_pd, 0, 0, 0)
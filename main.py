from sys import argv

def cargar_archivo(archivo):
    with open(archivo) as f:
        n =  int(f.readline())
        enemigos = [int(f.readline()) for _ in range(n)]
        potencias = [int(f.readline()) for _ in range(n)]
    return enemigos, potencias

def obtener_optimos(enemigos, potencias):
    n = len(enemigos)
    optimos = [0]*(n+1)
    #Se iteran todos los optimos
    for i in range(1, n + 1):
        maximo = 0
        #Se recorren los minutos para encontrar todos los valores posibles sumado al ataque final y se queda con el mayor
        for k in range(i):
            valor_actual = optimos[k] + min(enemigos[i - 1], potencias[i - 1 - k])
            maximo = max(valor_actual, maximo)
        optimos[i] = maximo
    return optimos

#dejo lo que teniamos antes comentado por las dudas
    #for i in range(1, len(optimos)):
        # OPT(n) = max(OPT(0) + min(x_n, f(n)), OPT(1) + min(x_n, f(n-1)), ... , OPT(n-1) + min(x_n, f(1)))
        #optimos[i] = max(map(lambda opt, k: opt + min(enemigos[i-1],potencias[i-1-k]), optimos[:i], range(i))) # O(n)

# Devuelve los minutos en los cuales se debe atacar

def construir_estrategia(enemigos, potencias, optimos):
    solucion = []
    i = len(enemigos)
    #Se arranca de atras para adelante
    while i > 0:
        solucion.append(i)
        #Se recorren los valores posibles para llegar al optimo actual
        for k in range(i):
            valor = optimos[k] + min(enemigos[i - 1], potencias[i - 1 - k])
            #Aquel que sea igual al optimos[i] que estamos mirando, es la ubicacion donde atacamos por ultima vez (sin contar la actual)
            if valor == optimos[i]:
                #Actualizamos indice yendo a esa ubicacion
                i = k
                break    
    solucion.reverse()
    return solucion

   #dejo comentado por las dudas 
    #while i > 0:
       # solucion.append(i)
       # anteriores = list(map(lambda opt, k: opt + min(enemigos[i-1],potencias[i-1-k]), optimos[:i], range(i)))
       # i = anteriores.index(optimos[i])
   # return list(reversed(solucion))

if __name__ == "__main__":
    enemigos, potencias = cargar_archivo(argv[1])
    optimos = obtener_optimos(enemigos, potencias)
    print("Estrategia (minutos en los que atacar):", construir_estrategia(enemigos, potencias, optimos))
    print("Cantidad de tropas eliminadas:", optimos[-1])

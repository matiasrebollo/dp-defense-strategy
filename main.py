from sys import argv

def cargar_archivo(archivo):
    with open(archivo) as f:
        n =  int(f.readline())
        ataques = [int(f.readline()) for _ in range(n)]
        potencias = [int(f.readline()) for _ in range(n)]
    return ataques, potencias

def obtener_optimos(ataques, potencias):
    n = len(ataques)
    optimos = [0]*(n+1)
    for i in range(1, n + 1):
        maximo = 0
        for k in range(i):
            valor_actual = optimos[k] + min(ataques[i - 1], potencias[i - 1 - k])
            if valor_actual > maximo:
                maximo = valor_actual
        optimos[i] = maximo
    return optimos

#dejo lo que teniamos antes comentado por las dudas
    #for i in range(1, len(optimos)):
        # OPT(n) = max(OPT(0) + min(x_n, f(n)), OPT(1) + min(x_n, f(n-1)), ... , OPT(n-1) + min(x_n, f(1)))
        #optimos[i] = max(map(lambda opt, k: opt + min(ataques[i-1],potencias[i-1-k]), optimos[:i], range(i))) # O(n)

# Devuelve los minutos en los cuales se debe atacar

def construir_estrategia(ataques, potencias, optimos):
    solucion = []
    i = len(optimos) - 1
    while i > 0:
        solucion.append(i)
        posibles_optimos = []
        for k in range(i):
            valor = optimos[k] + min(ataques[i - 1], potencias[i - 1 - k])
            posibles_optimos.append(valor)
        for k in range(i):
            if posibles_optimos[k] == optimos[i]:
                i = k
                break
    solucion.reverse()
    return [x - 1 for x in solucion]

   #dejo comentado por las dudas 
    #while i > 0:
       # solucion.append(i)
       # anteriores = list(map(lambda opt, k: opt + min(ataques[i-1],potencias[i-1-k]), optimos[:i], range(i)))
       # i = anteriores.index(optimos[i])
   # return list(reversed(solucion))

if __name__ == "__main__":
    ataques, potencias = cargar_archivo(argv[1])
    optimos = obtener_optimos(ataques, potencias)
    print("Estrategia (minutos en los que atacar):", construir_estrategia(ataques, potencias, optimos))
    print("Cantidad de tropas eliminadas:", optimos[-1])

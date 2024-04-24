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
    for i in range(1, len(optimos)):
        # OPT(n) = max(OPT(0) + min(x_n, f(n)), OPT(1) + min(x_n, f(n-1)), ... , OPT(n-1) + min(x_n, f(1)))
        optimos[i] = max(map(lambda opt, c: opt + min(ataques[i-1],potencias[i-c-1]), optimos[:i], range(i))) # O(n)
    return optimos

# Devuelve los minutos en los cuales se debe atacar
def construir_estrategia(ataques, potencias, optimos):
    solucion = []
    i = len(optimos)-1
    while i > 0:
        solucion.append(i)
        anteriores = list(map(lambda opt, c: opt + min(ataques[i-1],potencias[i-c-1]), optimos[:i], range(i)))
        i = anteriores.index(optimos[i])
    return list(reversed(solucion))

if __name__ == "__main__":
    ataques, potencias = cargar_archivo(argv[1])
    optimos = obtener_optimos(ataques, potencias)
    print("Estrategia (minutos en los que atacar):", construir_estrategia(ataques, potencias, optimos))
    print("Cantidad de tropas eliminadas:", optimos[-1])
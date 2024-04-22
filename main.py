from sys import argv

def cargar_archivo(archivo):
    with open(archivo) as f:
        n =  int(f.readline())
        ataques = [int(f.readline()) for _ in range(n)]
        potencias = [int(f.readline()) for _ in range(n)]
    return ataques, potencias

def obtener_optimo(ataques, potencias):
    n = len(ataques)
    optimo = [0]*(n+1)
    for i in range(1, len(optimo)):
        # OPT(n) = max(OPT(0) + min(x_n, f(n)), OPT(1) + min(x_n, f(n-1)), ... , OPT(n-1) + min(x_n, f(1)))
        optimo[i] = max(map(lambda x, c: x + min(ataques[i-1],potencias[i-c-1]), optimo[:i], range(i))) # O(n)
    return optimo

if __name__ == "__main__":
    ataques, potencias = cargar_archivo(argv[1])
    max_eliminados = obtener_optimo(ataques, potencias)[-1]
    print("Cantidad de tropas eliminadas: ", max_eliminados)
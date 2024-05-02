import unittest
from main import cargar_archivo, construir_estrategia, obtener_optimos

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

def obtener_optimo_bt(enemigos, potencias, optimo, i, optimo_actual, ultimo_ataque):
    if i == len(enemigos):
        return optimo_actual
    
    if optimo_actual + sum(enemigos[i:]) <= optimo:
        return optimo
    
    nuevo_optimo = optimo_actual + min(enemigos[i], potencias[i-ultimo_ataque])
    optimo_atacando = obtener_optimo_bt(enemigos, potencias, optimo, i+1, nuevo_optimo, i+1)
    optimo_sin_atacar = obtener_optimo_bt(enemigos, potencias, optimo, i+1, optimo_actual, ultimo_ataque)
    
    return max(optimo_atacando, optimo_sin_atacar)

def verificar_optimalidad(enemigos, potencias, optimo):
    return optimo == obtener_optimo_bt(enemigos, potencias, optimo, 0, 0, 0)

class Test(unittest.TestCase):
    def test_drive_5(self):
        enemigos, potencias = cargar_archivo('pruebas_drive/5.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 1413)
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 1413)
        assert verificar_optimalidad(enemigos, potencias, optimos[-1])             
        
    def test_drive_10(self):
        enemigos, potencias = cargar_archivo('pruebas_drive/10.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 2118)
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 2118)
        assert verificar_optimalidad(enemigos, potencias, optimos[-1])              

    def test_drive_10_bis(self):
        enemigos, potencias = cargar_archivo('pruebas_drive/10_bis.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 1237)
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 1237)
        assert verificar_optimalidad(enemigos, potencias, optimos[-1])              

    def test_drive_20(self):
        enemigos, potencias = cargar_archivo('pruebas_drive/20.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 11603)
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 11603)
        assert verificar_optimalidad(enemigos, potencias, optimos[-1])               

    def test_drive_50(self):
        enemigos, potencias = cargar_archivo('pruebas_drive/50.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 3994)
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 3994)

    def test_drive_100(self):
        enemigos, potencias = cargar_archivo('pruebas_drive/100.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 7492)
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 7492)

    def test_drive_200(self):
        enemigos, potencias = cargar_archivo('pruebas_drive/200.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 4230)
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 4230)

    def test_drive_500(self):
        enemigos, potencias = cargar_archivo('pruebas_drive/500.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 15842)
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 15842)

    def test_drive_1000(self):
        enemigos, potencias = cargar_archivo('pruebas_drive/1000.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 4508)
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 4508)

    def test_drive_5000(self):
        enemigos, potencias = cargar_archivo('pruebas_drive/5000.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 504220)
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 504220)        

if __name__ == '__main__':
    unittest.main()
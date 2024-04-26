import unittest
from main import cargar_archivo, construir_estrategia, obtener_optimos

def calcular_tropas_eliminadas(ataques, potencias, estrategia):
        cant_tropas = 0
        potencia = 1
        for i in range(1, len(ataques)+1):
            if i in estrategia:
                cant_tropas += min(ataques[i-1], potencias[potencia-1])
                potencia = 1
            else: 
                potencia += 1

        return cant_tropas

class Test(unittest.TestCase):
    def test_drive_5(self):
        ataques, potencias = cargar_archivo('pruebas_drive/5.txt')
        optimos = obtener_optimos(ataques, potencias)
        estrategia = construir_estrategia(ataques, potencias, optimos)
        self.assertEqual(optimos[-1], 1413)
        self.assertEqual(calcular_tropas_eliminadas(ataques, potencias, estrategia), 1413)
        
    def test_drive_10(self):
        ataques, potencias = cargar_archivo('pruebas_drive/10.txt')
        optimos = obtener_optimos(ataques, potencias)
        estrategia = construir_estrategia(ataques, potencias, optimos)
        self.assertEqual(optimos[-1], 2118)
        self.assertEqual(calcular_tropas_eliminadas(ataques, potencias, estrategia), 2118)

    def test_drive_10_bis(self):
        ataques, potencias = cargar_archivo('pruebas_drive/10_bis.txt')
        optimos = obtener_optimos(ataques, potencias)
        estrategia = construir_estrategia(ataques, potencias, optimos)
        self.assertEqual(optimos[-1], 1237)
        self.assertEqual(calcular_tropas_eliminadas(ataques, potencias, estrategia), 1237)

    def test_drive_20(self):
        ataques, potencias = cargar_archivo('pruebas_drive/20.txt')
        optimos = obtener_optimos(ataques, potencias)
        estrategia = construir_estrategia(ataques, potencias, optimos)
        self.assertEqual(optimos[-1], 11603)
        self.assertEqual(calcular_tropas_eliminadas(ataques, potencias, estrategia), 11603)

    def test_drive_50(self):
        ataques, potencias = cargar_archivo('pruebas_drive/50.txt')
        optimos = obtener_optimos(ataques, potencias)
        estrategia = construir_estrategia(ataques, potencias, optimos)
        self.assertEqual(optimos[-1], 3994)
        self.assertEqual(calcular_tropas_eliminadas(ataques, potencias, estrategia), 3994)

    def test_drive_100(self):
        ataques, potencias = cargar_archivo('pruebas_drive/100.txt')
        optimos = obtener_optimos(ataques, potencias)
        estrategia = construir_estrategia(ataques, potencias, optimos)
        self.assertEqual(optimos[-1], 7492)
        self.assertEqual(calcular_tropas_eliminadas(ataques, potencias, estrategia), 7492)

    def test_drive_200(self):
        ataques, potencias = cargar_archivo('pruebas_drive/200.txt')
        optimos = obtener_optimos(ataques, potencias)
        estrategia = construir_estrategia(ataques, potencias, optimos)
        self.assertEqual(optimos[-1], 4230)
        self.assertEqual(calcular_tropas_eliminadas(ataques, potencias, estrategia), 4230)

    def test_drive_500(self):
        ataques, potencias = cargar_archivo('pruebas_drive/500.txt')
        optimos = obtener_optimos(ataques, potencias)
        estrategia = construir_estrategia(ataques, potencias, optimos)
        self.assertEqual(optimos[-1], 15842)
        self.assertEqual(calcular_tropas_eliminadas(ataques, potencias, estrategia), 15842)

    def test_drive_1000(self):
        ataques, potencias = cargar_archivo('pruebas_drive/1000.txt')
        optimos = obtener_optimos(ataques, potencias)
        estrategia = construir_estrategia(ataques, potencias, optimos)
        self.assertEqual(optimos[-1], 4508)
        self.assertEqual(calcular_tropas_eliminadas(ataques, potencias, estrategia), 4508)

    def test_drive_5000(self):
        ataques, potencias = cargar_archivo('pruebas_drive/5000.txt')
        optimos = obtener_optimos(ataques, potencias)
        estrategia = construir_estrategia(ataques, potencias, optimos)
        self.assertEqual(optimos[-1], 504220)
        self.assertEqual(calcular_tropas_eliminadas(ataques, potencias, estrategia), 504220)        

if __name__ == '__main__':
    unittest.main()
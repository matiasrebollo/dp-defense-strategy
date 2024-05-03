import unittest
from main import cargar_archivo, construir_estrategia, obtener_optimos
from utils import calcular_tropas_eliminadas, verificar_optimalidad  

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
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

    def test_1(self):
        enemigos, potencias = cargar_archivo('ejemplos/1.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 33)
        self.assertEqual(estrategia, [1])
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 33)  

    def test_enemigos_constantes(self):
        enemigos, potencias = cargar_archivo('ejemplos/Enemigos constantes.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 220)
        self.assertEqual(estrategia, [2, 12, 22])
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 220) 

    def test_enemigos_crecientes(self):
        enemigos, potencias = cargar_archivo('ejemplos/Enemigos crecientes.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 1010)
        self.assertEqual(estrategia, [2, 11])
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 1010)

    def test_enemigos_decrecientes(self):
        enemigos, potencias = cargar_archivo('ejemplos/Enemigos decrecientes.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 370)
        self.assertEqual(estrategia, [6, 9, 10])
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 370)

    def test_numeros_muy_grandes(self):
        enemigos, potencias = cargar_archivo('ejemplos/Numeros muy grandes.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 5446736325)
        self.assertEqual(estrategia, [1, 2, 3, 4, 5])
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 5446736325)

    def test_enemigos_variaciones(self):
        enemigos, potencias = cargar_archivo('ejemplos/Variaciones de enemigos.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 2561)
        self.assertEqual(estrategia, [7, 8])
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 2561)

    def test_enemigos_vacio(self):
        enemigos, potencias = cargar_archivo('ejemplos/Vector vacio.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 0)
        self.assertEqual(estrategia, [])
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 0)
    

if __name__ == '__main__':
    unittest.main()

import unittest
from main import cargar_archivo, construir_estrategia, obtener_optimos
from utils import calcular_tropas_eliminadas, obtener_optimo_bt  

class Test(unittest.TestCase):
    def test_drive_5(self):
        enemigos, potencias = cargar_archivo('pruebas_drive/5.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 1413)
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 1413)
        self.assertEqual(optimos[-1], obtener_optimo_bt(enemigos, potencias, optimos[-1], 0, 0, 0))        
        
    def test_drive_10(self):
        enemigos, potencias = cargar_archivo('pruebas_drive/10.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 2118)
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 2118)
        self.assertEqual(optimos[-1], obtener_optimo_bt(enemigos, potencias, optimos[-1], 0, 0, 0))        

    def test_drive_10_bis(self):
        enemigos, potencias = cargar_archivo('pruebas_drive/10_bis.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 1237)
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 1237)
        self.assertEqual(optimos[-1], obtener_optimo_bt(enemigos, potencias, optimos[-1], 0, 0, 0))        

    def test_drive_20(self):
        enemigos, potencias = cargar_archivo('pruebas_drive/20.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], 11603)
        self.assertEqual(calcular_tropas_eliminadas(enemigos, potencias, estrategia), 11603)
        self.assertEqual(optimos[-1], obtener_optimo_bt(enemigos, potencias, optimos[-1], 0, 0, 0))        

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
        self.assertEqual(optimos[-1], obtener_optimo_bt(enemigos, potencias, 0, 0, 0, 0))        
        self.assertEqual(optimos[-1], calcular_tropas_eliminadas(enemigos, potencias, estrategia))

    def test_2(self):
        enemigos, potencias = cargar_archivo('ejemplos/2.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], obtener_optimo_bt(enemigos, potencias, 0, 0, 0, 0))        
        self.assertEqual(optimos[-1], calcular_tropas_eliminadas(enemigos, potencias, estrategia))

    def test_enemigos_constantes(self):
        enemigos, potencias = cargar_archivo('ejemplos/Enemigos constantes.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], obtener_optimo_bt(enemigos, potencias, 0, 0, 0, 0))        
        self.assertEqual(optimos[-1], calcular_tropas_eliminadas(enemigos, potencias, estrategia))

    def test_enemigos_crecientes(self):
        enemigos, potencias = cargar_archivo('ejemplos/Enemigos crecientes.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], obtener_optimo_bt(enemigos, potencias, 0, 0, 0, 0))        
        self.assertEqual(optimos[-1], calcular_tropas_eliminadas(enemigos, potencias, estrategia))

    def test_enemigos_decrecientes(self):
        enemigos, potencias = cargar_archivo('ejemplos/Enemigos decrecientes.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], obtener_optimo_bt(enemigos, potencias, 0, 0, 0, 0))        
        self.assertEqual(optimos[-1], calcular_tropas_eliminadas(enemigos, potencias, estrategia))

    def test_numeros_muy_grandes(self):
        enemigos, potencias = cargar_archivo('ejemplos/Numeros muy grandes.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], obtener_optimo_bt(enemigos, potencias, 0, 0, 0, 0))        
        self.assertEqual(optimos[-1], calcular_tropas_eliminadas(enemigos, potencias, estrategia))

    def test_enemigos_variaciones(self):
        enemigos, potencias = cargar_archivo('ejemplos/Variaciones de enemigos.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], obtener_optimo_bt(enemigos, potencias, 0, 0, 0, 0))        
        self.assertEqual(optimos[-1], calcular_tropas_eliminadas(enemigos, potencias, estrategia))

    def test_enemigos_vacio(self):
        enemigos, potencias = cargar_archivo('ejemplos/Vector vacio.txt')
        optimos = obtener_optimos(enemigos, potencias)
        estrategia = construir_estrategia(enemigos, potencias, optimos)
        self.assertEqual(optimos[-1], obtener_optimo_bt(enemigos, potencias, 0, 0, 0, 0))        
        self.assertEqual(optimos[-1], calcular_tropas_eliminadas(enemigos, potencias, estrategia))
    
if __name__ == '__main__':
    unittest.main()

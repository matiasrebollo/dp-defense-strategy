import unittest
from main import cargar_archivo, obtener_optimos

class Test(unittest.TestCase):
    def test_drive_5(self):
        ataques, potencias = cargar_archivo('pruebas_drive/5.txt')
        optimos = obtener_optimos(ataques, potencias)
        self.assertEqual(optimos[-1], 1413)
        
    def test_drive_10(self):
        ataques, potencias = cargar_archivo('pruebas_drive/10.txt')
        optimos = obtener_optimos(ataques, potencias)
        self.assertEqual(optimos[-1], 2118)

    def test_drive_10_bis(self):
        ataques, potencias = cargar_archivo('pruebas_drive/10_bis.txt')
        optimos = obtener_optimos(ataques, potencias)
        self.assertEqual(optimos[-1], 1237)

    def test_drive_20(self):
        ataques, potencias = cargar_archivo('pruebas_drive/20.txt')
        optimos = obtener_optimos(ataques, potencias)
        self.assertEqual(optimos[-1], 11603)

    def test_drive_50(self):
        ataques, potencias = cargar_archivo('pruebas_drive/50.txt')
        optimos = obtener_optimos(ataques, potencias)
        self.assertEqual(optimos[-1], 3994)

    def test_drive_100(self):
        ataques, potencias = cargar_archivo('pruebas_drive/100.txt')
        optimos = obtener_optimos(ataques, potencias)
        self.assertEqual(optimos[-1], 7492)

    def test_drive_200(self):
        ataques, potencias = cargar_archivo('pruebas_drive/200.txt')
        optimos = obtener_optimos(ataques, potencias)
        self.assertEqual(optimos[-1], 4230)

    def test_drive_500(self):
        ataques, potencias = cargar_archivo('pruebas_drive/500.txt')
        optimos = obtener_optimos(ataques, potencias)
        self.assertEqual(optimos[-1], 15842)

    def test_drive_1000(self):
        ataques, potencias = cargar_archivo('pruebas_drive/1000.txt')
        optimos = obtener_optimos(ataques, potencias)
        self.assertEqual(optimos[-1], 4508)

    def test_drive_5000(self):
        ataques, potencias = cargar_archivo('pruebas_drive/5000.txt')
        optimos = obtener_optimos(ataques, potencias)
        self.assertEqual(optimos[-1], 504220)        

if __name__ == '__main__':
    unittest.main()
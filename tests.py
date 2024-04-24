import unittest
from main import cargar_archivo, obtener_optimos

class Test(unittest.TestCase):
    def test_drive_5(self):
        ataques, potencias = cargar_archivo('pruebas_drive/5.txt')
        optimos = obtener_optimos(ataques, potencias)
        self.assertEqual(optimos[-1], 1413)

if __name__ == '__main__':
    unittest.main()
import unittest
from main import cargar_archivo, obtener_optimo

class Test(unittest.TestCase):
    def test_drive_5(self):
        ataques, potencias = cargar_archivo('pruebas_drive/5.txt')
        optimo = obtener_optimo(ataques, potencias)
        self.assertEqual(optimo[-1], 1413)

if __name__ == '__main__':
    unittest.main()
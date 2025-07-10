
import unittest
from main import multa_localidade, multa_fora_localidade, multa_autoestrada

class TestMultas(unittest.TestCase):

    def test_localidade_sem_multa(self):
        self.assertEqual(multa_localidade(45), 0)

    def test_localidade_multa_moderada(self):
        self.assertEqual(multa_localidade(85), 60)

    def test_localidade_multa_grave(self):
        self.assertEqual(multa_localidade(95), 120)

    def test_localidade_multa_muito_grave(self):
        self.assertEqual(multa_localidade(130), 320)

    def test_fora_localidade_sem_multa(self):
        self.assertEqual(multa_fora_localidade(80), 0)

    def test_fora_localidade_multa_moderada(self):
        self.assertEqual(multa_fora_localidade(100), 60)

    def test_fora_localidade_multa_grave(self):
        self.assertEqual(multa_fora_localidade(125), 120)

    def test_autoestrada_sem_multa(self):
        self.assertEqual(multa_autoestrada(110), 0)

    def test_autoestrada_multa_moderada(self):
        self.assertEqual(multa_autoestrada(130), 60)

    def test_autoestrada_multa_grave(self):
        self.assertEqual(multa_autoestrada(160), 120)

    def test_autoestrada_multa_muito_grave(self):
        self.assertEqual(multa_autoestrada(180), 360)

if __name__ == '__main__':
    unittest.main()

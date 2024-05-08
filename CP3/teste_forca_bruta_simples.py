import unittest
from forca_bruta import forca_bruta

class TestForcaBruta(unittest.TestCase):
    def test_forca_bruta_senha_curta(self):
        senha_curta = 'abc'
        resultado = forca_bruta(senha_curta, caracteres_forca_bruta, 1, 5)
        self.assertIsNone(resultado)

    def test_forca_bruta_senha_media(self):
        senha_media = 'senha123'
        resultado = forca_bruta(senha_media, caracteres_forca_bruta, 1, 5)
        self.assertIsNone(resultado)

    # Adicione mais testes conforme necessário

if __name__ == '__main__':
    unittest.main()

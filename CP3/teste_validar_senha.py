import unittest
from validacao_senha import validar_senha

class TestValidarSenha(unittest.TestCase):
    def test_senha_forte(self):
        self.assertTrue(validar_senha("Senha@123", min_caracteres=8, min_especiais=1, min_numeros=1, min_maiusculas=1))
    
    def test_senha_fraca(self):
        self.assertFalse(validar_senha("senhafraca", min_caracteres=8, min_especiais=1, min_numeros=1, min_maiusculas=1))
    
    def test_senha_numeros(self):
        self.assertFalse(validar_senha("senha12345", min_caracteres=8, min_especiais=1, min_numeros=1, min_maiusculas=1))

    def test_senha_caracteres_especiais(self):
        self.assertFalse(validar_senha("senha@especial", min_caracteres=8, min_especiais=1, min_numeros=1, min_maiusculas=1))

    def test_senha_maiusculas(self):
        self.assertTrue(validar_senha("senhaUpper@1", min_caracteres=8, min_especiais=1, min_numeros=1, min_maiusculas=1))

    def test_senha_combinacao_fraca(self):
        self.assertFalse(validar_senha("senhafraca123", min_caracteres=8, min_especiais=1, min_numeros=1, min_maiusculas=1))

    def test_senha_combinacao_forte(self):
        self.assertTrue(validar_senha("Senha123@#$", min_caracteres=8, min_especiais=1, min_numeros=1, min_maiusculas=1))

    def test_senha_todos_especiais(self):
        self.assertFalse(validar_senha("!@#$%^&*()_+{}[]|\:;'<>?,./", min_caracteres=8, min_especiais=1, min_numeros=1, min_maiusculas=1))

    def test_senha_todos_numeros(self):
        self.assertFalse(validar_senha("1234567890", min_caracteres=8, min_especiais=1, min_numeros=1, min_maiusculas=1))

    def test_senha_todas_maiusculas(self):
        self.assertFalse(validar_senha("SENHAFORTE", min_caracteres=8, min_especiais=1, min_numeros=1, min_maiusculas=1))

if __name__ == '__main__':
    unittest.main()

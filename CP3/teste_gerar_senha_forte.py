import unittest
import string
from gerador_senha import gerar_senha

class TestGerarSenhaForte(unittest.TestCase):
    def teste_tamanho_senha_minimo(self):
        senha = gerar_senha(8, 12, 2, 2, 2)
        self.assertGreaterEqual(len(senha), 8)

    def teste_tamanho_senha_maximo(self):
        senha = gerar_senha(8, 12, 2, 2, 2)
        self.assertLessEqual(len(senha), 12)

    def teste_qtd_caracteres_especiais(self):
        senha = gerar_senha(8, 12, 2, 2, 2)
        qtd_especiais = sum(c.isascii() and not c.isalnum() for c in senha)
        self.assertGreaterEqual(qtd_especiais, 2)

    def teste_qtd_numeros(self):
        senha = gerar_senha(8, 12, 2, 2, 2)
        qtd_numeros = sum(c.isdigit() for c in senha)
        self.assertEqual(qtd_numeros, 2)

    def teste_qtd_maiusculas(self):
        senha = gerar_senha(8, 12, 2, 2, 2)
        qtd_maiusculas = sum(c.isupper() for c in senha)
        self.assertGreaterEqual(qtd_maiusculas, 2)

    def teste_senha_caracteres_especiais(self):
        senha = gerar_senha(8, 12, 2, 2, 2)
        caracteres_especiais = string.punctuation
        self.assertTrue(any(c in caracteres_especiais for c in senha))

    def teste_senha_numeros(self):
        senha = gerar_senha(8, 12, 2, 2, 2)
        numeros = string.digits
        self.assertTrue(any(c in numeros for c in senha))

    def teste_senha_maiusculas(self):
        senha = gerar_senha(8, 12, 2, 2, 2)
        maiusculas = string.ascii_uppercase
        self.assertTrue(any(c in maiusculas for c in senha))

    def teste_senha_minusculas(self):
        senha = gerar_senha(8, 12, 2, 2, 2)
        minusculas = string.ascii_lowercase
        self.assertTrue(any(c in minusculas for c in senha))

    def teste_senha_caracteres_invalidos(self):
        senha = gerar_senha(8, 12, 2, 2, 2)
        caracteres_invalidos = set(senha) - set(string.ascii_letters + string.digits + string.punctuation)
        self.assertFalse(caracteres_invalidos)

    def teste_senha_unicidade(self):
        senha1 = gerar_senha(8, 12, 2, 2, 2)
        senha2 = gerar_senha(8, 12, 2, 2, 2)
        self.assertNotEqual(senha1, senha2)

if __name__ == '__main__':
    unittest.main()

import unittest
from ataque_forca_bruta import ataque_bruteforce


class TesteForcaBrutaSenha(unittest.TestCase):
    def test_forca_bruta_senha(self):
        def verificar_senha(senha):
            return senha == "Senha@123"
        senha_encontrada = ataque_bruteforce(verificar_senha, max_comprimento=8)
        self.assertEqual(senha_encontrada, "Senha@123")

    def test_forca_bruta_senha_nao_encontrada(self):
        def verificar_senha(senha):
            return senha == "senha_que_nao_existe"
        senha_encontrada = ataque_bruteforce(verificar_senha, max_comprimento=4)
        self.assertIsNone(senha_encontrada)

    def test_forca_bruta_senha_vazia(self):
        def verificar_senha(senha):
            return senha == ""
        senha_encontrada = ataque_bruteforce(verificar_senha, max_comprimento=0)
        self.assertEqual(senha_encontrada, "")

    def test_forca_bruta_senha_curta(self):
        def verificar_senha(senha):
            return senha == "a1!"
        senha_encontrada = ataque_bruteforce(verificar_senha, max_comprimento=3)
        self.assertEqual(senha_encontrada, "a1!")

    def test_forca_bruta_senha_longa(self):
        def verificar_senha(senha):
            return senha == "abc123!"
        senha_encontrada = ataque_bruteforce(verificar_senha, max_comprimento=7)
        self.assertEqual(senha_encontrada, "abc123!")

    def test_forca_bruta_senha_alfanumerica(self):
        def verificar_senha(senha):
            return senha == "abc123"
        senha_encontrada = ataque_bruteforce(verificar_senha, max_comprimento=6)
        self.assertEqual(senha_encontrada, "abc123")

    def test_forca_bruta_senha_caracteres_especiais(self):
        def verificar_senha(senha):
            return senha == "!@#"
        senha_encontrada = ataque_bruteforce(verificar_senha, max_comprimento=3)
        self.assertEqual(senha_encontrada, "!@#")

    def test_forca_bruta_senha_caracteres_mistos(self):
        def verificar_senha(senha):
            return senha == "A1!a"
        senha_encontrada = ataque_bruteforce(verificar_senha, max_comprimento=4)
        self.assertEqual(senha_encontrada, "A1!a")

    def test_forca_bruta_senha_case_sensitive(self):
        def verificar_senha(senha):
            return senha == "Aa1!"
        senha_encontrada = ataque_bruteforce(verificar_senha, max_comprimento=4)
        self.assertEqual(senha_encontrada, "Aa1!")

    def test_forca_bruta_senha_com_espaco(self):
        def verificar_senha(senha):
            return senha == "a 1"
        senha_encontrada = ataque_bruteforce(verificar_senha, max_comprimento=3)
        self.assertEqual(senha_encontrada, "a 1")

if __name__ == '__main__':
    unittest.main()

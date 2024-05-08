import unittest
from cryptography.fernet import Fernet
from encriptacao_arquivo import encriptar_arquivo, desencriptar_arquivo

class TestEncriptacaoArquivos(unittest.TestCase):
    def setUp(self):
        # Cria arquivos vazios para os testes
        open('arquivo.txt', 'w').close()
        open('arquivo_encriptado.txt', 'w').close()
        open('arquivo_desencriptado.txt', 'w').close()
        open('arquivo_encriptado_chave_gerada.txt', 'w').close()
        open('arquivo_desencriptado_chave_gerada.txt', 'w').close()
        open('arquivo_encriptado_senha_incorreta.txt', 'w').close()
        open('arquivo_desencriptado_senha_incorreta.txt', 'w').close()

    def test_encriptar_desencriptar_arquivo(self):
        # Teste de encriptação e desencriptação de um arquivo
        arquivo_original = 'arquivo.txt'
        senha = Fernet.generate_key()
        arquivo_encriptado = 'arquivo_encriptado.txt'
        encriptar_arquivo(arquivo_original, arquivo_encriptado, senha)
        desencriptar_arquivo(arquivo_encriptado, 'arquivo_desencriptado.txt', senha)

        # Verifica se o arquivo desencriptado é igual ao original
        with open(arquivo_original, 'r') as original, open('arquivo_desencriptado.txt', 'r') as desencriptado:
            self.assertEqual(original.read(), desencriptado.read())

    def test_encriptar_desencriptar_arquivo_com_chave_gerada(self):
        # Teste de encriptação e desencriptação de um arquivo usando chave gerada
        arquivo_original = 'arquivo.txt'
        senha_encriptacao = Fernet.generate_key()
        arquivo_encriptado = 'arquivo_encriptado_chave_gerada.txt'
        encriptar_arquivo(arquivo_original, arquivo_encriptado, senha_encriptacao)
        desencriptar_arquivo(arquivo_encriptado, 'arquivo_desencriptado_chave_gerada.txt', senha_encriptacao)

        # Verifica se o arquivo desencriptado é igual ao original
        with open(arquivo_original, 'r') as original, open('arquivo_desencriptado_chave_gerada.txt', 'r') as desencriptado:
            self.assertEqual(original.read(), desencriptado.read())

    def test_encriptar_arquivo_com_senha_incorreta(self):
        # Teste de encriptação com senha incorreta
        arquivo_original = 'arquivo.txt'
        senha_correta = Fernet.generate_key()
        senha_incorreta = Fernet.generate_key()
        arquivo_encriptado = 'arquivo_encriptado_senha_incorreta.txt'
        encriptar_arquivo(arquivo_original, arquivo_encriptado, senha_correta)

        # Tentativa de desencriptação com senha incorreta
        with self.assertRaises(Exception):
            desencriptar_arquivo(arquivo_encriptado, 'arquivo_desencriptado_senha_incorreta.txt', senha_incorreta)

if __name__ == '__main__':
    unittest.main()

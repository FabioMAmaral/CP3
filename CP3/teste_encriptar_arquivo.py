import unittest
import os
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
from encriptacao_arquivo import encriptar_arquivo
from decriptacao_arquivo import descriptar_arquivo

class TestEncriptacaoArquivos(unittest.TestCase):
    def setUp(self):
        self.diretorio_teste = "diretorio_teste"
        os.makedirs(self.diretorio_teste, exist_ok=True)
        self.chave = Fernet.generate_key()

    def tearDown(self):
        if os.path.exists(self.diretorio_teste):
            os.rmdir(self.diretorio_teste)

    def test_encriptacao_basica(self):
        arquivo_teste = os.path.join(self.diretorio_teste, "arquivo_teste.txt")
        with open(arquivo_teste, "w") as file:
            file.write("Conteúdo do arquivo de teste")
        encriptar_arquivo(arquivo_teste, self.chave)
        arquivo_encriptado = arquivo_teste + ".enc"
        self.assertTrue(os.path.exists(arquivo_encriptado))
        self.assertTrue(os.path.getsize(arquivo_encriptado) > os.path.getsize(arquivo_teste))

    def test_encriptacao_e_descriptacao(self):
        arquivo_teste = os.path.join(self.diretorio_teste, "arquivo_teste.txt")
        with open(arquivo_teste, "w") as file:
            file.write("Conteúdo do arquivo de teste")
        encriptar_arquivo(arquivo_teste, self.chave)
        descriptar_arquivo(arquivo_teste + ".enc", self.chave)
        with open(arquivo_teste, "r") as file:
            conteudo_original = file.read()
        with open(arquivo_teste + ".dec", "r") as file:
            conteudo_descriptado = file.read()
        self.assertEqual(conteudo_original, conteudo_descriptado)

    def test_encriptacao_em_lote(self):
        arquivos_teste = []
        for i in range(5):
            arquivo_teste = os.path.join(self.diretorio_teste, f"arquivo_teste_{i}.txt")
            with open(arquivo_teste, "w") as file:
                file.write(f"Conteúdo do arquivo de teste {i}")
            arquivos_teste.append(arquivo_teste)
        for arquivo in arquivos_teste:
            encriptar_arquivo(arquivo, self.chave)
        for arquivo in arquivos_teste:
            self.assertTrue(os.path.exists(arquivo + ".enc"))

    def test_arquivo_vazio(self):
        arquivo_vazio = os.path.join(self.diretorio_teste, "arquivo_vazio.txt")
        with open(arquivo_vazio, "w") as file:
            pass
        encriptar_arquivo(arquivo_vazio, self.chave)
        arquivo_encriptado = arquivo_vazio + ".enc"
        self.assertTrue(os.path.exists(arquivo_encriptado))
        self.assertEqual(os.path.getsize(arquivo_encriptado), 0)

    def test_arquivo_inexistente(self):
        arquivo_inexistente = os.path.join(self.diretorio_teste, "arquivo_inexistente.txt")
        with self.assertRaises(FileNotFoundError):
            encriptar_arquivo(arquivo_inexistente, self.chave)

    def test_arquivo_protegido(self):
        arquivo_protegido = os.path.join(self.diretorio_teste, "arquivo_protegido.txt")
        with open(arquivo_protegido, "w") as file:
            file.write("Conteúdo do arquivo protegido")
        os.chmod(arquivo_protegido, 0o444)
        with self.assertRaises(PermissionError):
            encriptar_arquivo(arquivo_protegido, self.chave)

    def test_chave_incorreta(self):
        arquivo_teste = os.path.join(self.diretorio_teste, "arquivo_teste.txt")
        with open(arquivo_teste, "w") as file:
            file.write("Conteúdo do arquivo de teste")
        chave_incorreta = Fernet.generate_key()
        encriptar_arquivo(arquivo_teste, chave_incorreta)
        with self.assertRaises(InvalidToken):
            descriptar_arquivo(arquivo_teste + ".enc", self.chave)

    def test_chave_correta(self):
        arquivo_teste = os.path.join(self.diretorio_teste, "arquivo_teste.txt")
        with open(arquivo_teste, "w") as file:
            file.write("Conteúdo do arquivo de teste")
        encriptar_arquivo(arquivo_teste, self.chave)
        descriptar_arquivo(arquivo_teste + ".enc", self.chave)
        with open(arquivo_teste, "r") as file:
            conteudo_original = file.read()
        with open(arquivo_teste + ".dec", "r") as file:
            conteudo_descriptado = file.read()
        self.assertEqual(conteudo_original, conteudo_descriptado)

    def test_chave_ausente(self):
        arquivo_teste = os.path.join(self.diretorio_teste, "arquivo_teste.txt")
        with open(arquivo_teste, "w") as file:
            file.write("Conteúdo do arquivo de teste")
        encriptar_arquivo(arquivo_teste, self.chave)
        os.remove("secret.key")
        with self.assertRaises(InvalidToken):
            descriptar_arquivo(arquivo_teste + ".enc", self.chave)

    def test_diretorio_valido(self):
        diretorio_valido = os.path.join(self.diretorio_teste, "subdiretorio")
        os.makedirs(diretorio_valido, exist_ok=True)
        arquivo_teste = os.path.join(diretorio_valido, "arquivo_teste.txt")
        with open(arquivo_teste, "w") as file:
            file.write("Conteúdo do arquivo de teste")
        encriptar_arquivo(diretorio_valido, self.chave)
        arquivo_encriptado = arquivo_teste + ".enc"
        self.assertTrue(os.path.exists(arquivo_encriptado))

if __name__ == "__main__":
    unittest.main()

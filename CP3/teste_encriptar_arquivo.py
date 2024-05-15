import unittest
import os
from encriptacao_arquivo import encriptacao_arquivo
from decriptacao_arquivo import decriptacao_arquivo

class TestArquivosTemporarios(unittest.TestCase):
    def test_encriptacao_descriptacao(self):
        diretorio = "./temp_test"
        os.mkdir(diretorio)
        with open(os.path.join(diretorio, "teste1.txt"), "w") as file:
            file.write("Conteudo do arquivo teste1")
        with open(os.path.join(diretorio, "teste2.txt"), "w") as file:
            file.write("Conteudo do arquivo teste2")
        encriptacao_arquivo(diretorio)
        for arquivo in os.listdir(diretorio):
            if arquivo.endswith(".txt"):
                with open(os.path.join(diretorio, arquivo), "rb") as file:
                    conteudo = file.read()
                    self.assertNotEqual(conteudo, "Conteudo do arquivo {}".format(arquivo.split('.')[0]).encode())
        decriptacao_arquivo(diretorio)

        for arquivo in os.listdir(diretorio):
            if arquivo.endswith(".txt"):
                with open(os.path.join(diretorio, arquivo), "r") as file:
                    conteudo = file.read()
                    self.assertEqual(conteudo, "Conteudo do arquivo {}".format(arquivo.split('.')[0]))

        for arquivo in os.listdir(diretorio):
            os.remove(os.path.join(diretorio, arquivo))
        os.rmdir(diretorio)

if __name__ == "__main__":
    unittest.main()

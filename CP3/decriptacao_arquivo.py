from cryptography.fernet import Fernet
import os

def descriptar_arquivo(arquivo, chave):
    with open(arquivo, "rb") as file:
        conteudo_encriptado = file.read()
    fernet = Fernet(chave)
    conteudo_descriptado = fernet.decrypt(conteudo_encriptado)
    with open(arquivo[:-4], "wb") as file:
        file.write(conteudo_descriptado)

diretorio = input("Qual diretório você gostaria de descriptografar? ")

chave = Fernet.generate_key()

for arquivo in os.listdir(diretorio):
    caminho_completo = os.path.join(diretorio, arquivo)
    if os.path.isfile(caminho_completo):
        descriptar_arquivo(caminho_completo, chave)

print("Arquivos descriptografados com sucesso.")

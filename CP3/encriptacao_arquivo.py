from cryptography.fernet import Fernet
import os

def encriptar_arquivo(arquivo, chave):
    with open(arquivo, "rb") as file:
        conteudo = file.read()
    fernet = Fernet(chave)
    arquivo_encriptado = fernet.encrypt(conteudo)
    with open(arquivo + ".enc", "wb") as file:
        file.write(arquivo_encriptado)

diretorio = input("Qual diretório você gostaria de criptografar? ")

chave = Fernet.generate_key()

for arquivo in os.listdir(diretorio):
    caminho_completo = os.path.join(diretorio, arquivo)
    if os.path.isfile(caminho_completo):
        encriptar_arquivo(caminho_completo, chave)

with open("secret.key", "wb") as segredo:
    segredo.write(chave)

print("Arquivos criptografados com sucesso.")

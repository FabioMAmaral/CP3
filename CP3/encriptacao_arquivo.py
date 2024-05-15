import cryptography
from cryptography.fernet import Fernet
import os

diretorio = input("Qual diretório você gostaria de criptografar? ")

arquivos = []
chave = Fernet.generate_key()

for arquivo in os.listdir(diretorio):
    caminho_completo = os.path.join(diretorio, arquivo)
    if arquivo in ["Encrypt.py", "secret.key", "Decrypt.py"]:
        continue
    if os.path.isfile(caminho_completo):
        arquivos.append(caminho_completo)

with open("secret.key", "wb") as segredo:
    segredo.write(chave)

for arquivo in arquivos:
    with open(arquivo, "rb") as alvo:
        conteudo = alvo.read()
    alvo_criptografado = Fernet(chave).encrypt(conteudo)
    with open(arquivo, "wb") as alvo:
        alvo.write(alvo_criptografado)

print("Arquivos criptografados com sucesso.")

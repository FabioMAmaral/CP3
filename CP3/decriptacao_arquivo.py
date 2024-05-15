import cryptography
from cryptography.fernet import Fernet as fernet
import os

arquivos = []
caminho = input("Qual diretório você gostaria de descriptografar? ")

for arquivo in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, arquivo)
    if arquivo in ["Encrypt.py", "secret.key", "Decrypt.py"]:
        continue
    if os.path.isfile(caminho_completo):
        arquivos.append(caminho_completo)
    
with open("secret.key", "rb") as chave:
    chave_secreta = chave.read()

for arquivo in arquivos:
    with open(arquivo, "rb") as alvo:
        conteudo = alvo.read()
    alvo_descriptografado = fernet(chave_secreta).decrypt(conteudo)
    with open(arquivo, "wb") as alvo:
        alvo.write(alvo_descriptografado)
print("Arquivos descriptografados com sucesso.")

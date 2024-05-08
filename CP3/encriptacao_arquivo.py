from cryptography.fernet import Fernet

# Gerar ou carregar a chave de criptografia
# Neste exemplo, estamos gerando uma chave aleatória
senha_encriptacao = Fernet.generate_key()
fernet = Fernet(senha_encriptacao)

def encriptar_arquivo(nome_arquivo, arquivo_encriptado):
    with open(nome_arquivo, 'rb') as file:
        arquivo = file.read()
    arquivo_encriptado = fernet.encrypt(arquivo)
    with open(arquivo_encriptado, 'wb') as encrypted_file:
        encrypted_file.write(arquivo_encriptado)

def desencriptar_arquivo(arquivo_encriptado, arquivo_desencriptado):
    with open(arquivo_encriptado, 'rb') as file:
        arquivo_encriptado = file.read()
    arquivo_desencriptado = fernet.decrypt(arquivo_encriptado)
    with open(arquivo_desencriptado, 'wb') as decrypted_file:
        decrypted_file.write(arquivo_desencriptado)

# Exemplo de uso
encriptar_arquivo('arquivo.txt', 'arquivo_encriptado.txt')
desencriptar_arquivo('arquivo_encriptado.txt', 'arquivo_desencriptado.txt')

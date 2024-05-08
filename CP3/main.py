import random
import string
from cryptography.fernet import Fernet
import os
import itertools

def gerar_senha(tam_min, tam_max, qtd_numeros, qtd_maiusculas):
    if tam_min > tam_max:
        raise ValueError("O tamanho mínimo da senha não pode ser maior que o tamanho máximo.")

    numeros = string.digits
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase

    senha = []

    senha.extend(random.choices(numeros, k=qtd_numeros))
    senha.extend(random.choices(letras_maiusculas, k=qtd_maiusculas))
    senha.extend(random.choices(letras_minusculas, k=tam_max - (qtd_numeros + qtd_maiusculas)))

    random.shuffle(senha)

    return ''.join(senha)

# Exemplo de uso
tamanho_minimo = 4
tamanho_maximo = 5
quantidade_numeros = 1
quantidade_maiusculas = 1

senha_gerada = gerar_senha(tamanho_minimo, tamanho_maximo, quantidade_numeros, quantidade_maiusculas)
print("Senha gerada:", senha_gerada)


def validar_senha(senha, qtd_numeros, qtd_maiusculas):
    pontos = qtd_numeros + qtd_maiusculas
    return pontos >= 8

# Exemplo de uso
senha_gerada = gerar_senha(tamanho_minimo, tamanho_maximo, quantidade_numeros, quantidade_maiusculas)
print("Senha gerada:", senha_gerada)

if validar_senha(senha_gerada, quantidade_numeros, quantidade_maiusculas):
    print("A senha é considerada forte.")
else:
    print("A senha não atende aos critérios de segurança.")


def encriptar_arquivo(arquivo_origem, arquivo_destino, chave):
    try:
        with open(arquivo_origem, 'rb') as f:
            dados = f.read()

        fernet = Fernet(chave)
        dados_encriptados = fernet.encrypt(dados)

        with open(arquivo_destino, 'wb') as f:
            f.write(dados_encriptados)

        print("Arquivo encriptado com sucesso!")
    except Exception as e:
        print(f"Erro ao encriptar arquivo: {e}")

# Exemplo de uso
arquivo_origem = 'arquivo.txt'
arquivo_destino = 'arquivo_encriptado.txt'

chave = Fernet.generate_key()

encriptar_arquivo(arquivo_origem, arquivo_destino, chave)


def salvar_senhas(senhas):
    with open('senhas.txt', 'w') as f:
        for senha in senhas:
            f.write(f"{senha}\n")

# Exemplo de uso
senhas_geradas = [senha_gerada]
salvar_senhas(senhas_geradas)
print("Senhas salvas em senhas.txt.")


def salvar_arquivo_encriptado(arquivo_origem, arquivo_destino, chave, senha_usada):
    try:
        encriptar_arquivo(arquivo_origem, arquivo_destino, chave)
        with open('senhas_usadas.txt', 'a') as f:
            f.write(f"{arquivo_destino}: {senha_usada}\n")
        print(f"Arquivo {arquivo_origem} encriptado e salvo em {arquivo_destino}.")
    except Exception as e:
        print(f"Erro ao salvar arquivo encriptado: {e}")

# Exemplo de uso
arquivo_origem = 'arquivo.txt'
arquivo_destino = 'arquivos_encriptados/arquivo_encriptado.txt'

salvar_arquivo_encriptado(arquivo_origem, arquivo_destino, chave, senha_gerada)

def forca_bruta_simples(senha_correta, tamanho_senha, max_tentativas):
    caracteres = string.ascii_lowercase + string.digits
    tentativas = 0

    for tentativa in itertools.product(caracteres, repeat=tamanho_senha):
        tentativas += 1
        senha_tentativa = ''.join(tentativa)

        if senha_tentativa == senha_correta:
            print(f"Senha encontrada após {tentativas} tentativas: {senha_tentativa}")
            break

        if tentativas >= max_tentativas:
            print(f"Limite de tentativas atingido ({max_tentativas}).")
            break

# Exemplo de uso
senha_correta = senha_gerada  # Use a senha gerada anteriormente como senha correta
tamanho_senha = len(senha_correta)
forca_bruta_simples(senha_correta, tamanho_senha)

import itertools
import string

def forca_bruta(senha, caracteres, tamanho_min, tamanho_max):
    for tamanho in range(tamanho_min, tamanho_max + 1):
        for tentativa in itertools.product(caracteres, repeat=tamanho):
            tentativa_senha = ''.join(tentativa)
            if tentativa_senha == senha:
                return tentativa_senha

    return None

if __name__ == "__main__":
    senha_gerada = input("Digite a senha gerada: ")
    caracteres_forca_bruta = string.ascii_letters + string.digits + string.punctuation
    resultado = forca_bruta(senha_gerada, caracteres_forca_bruta, 1, 5)
    if resultado:
        print("Senha encontrada:", resultado)
    else:
        print("Senha não encontrada.")

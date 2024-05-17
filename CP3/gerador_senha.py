import random
import string

def gerar_senha(tamanho_min, tamanho_max, num_caracteres_especiais, num_numeros, num_maiusculas):
    caracteres_especiais = string.punctuation
    numeros = string.digits
    maiusculas = string.ascii_uppercase
    todas_letras = string.ascii_letters
    
    tamanho = random.randint(tamanho_min, tamanho_max)
    
    senha = ''.join(random.choice(caracteres_especiais) for _ in range(num_caracteres_especiais))
    senha += ''.join(random.choice(numeros) for _ in range(num_numeros))
    senha += ''.join(random.choice(maiusculas) for _ in range(num_maiusculas))
    
    senha += ''.join(random.choice(todas_letras) for _ in range(tamanho - num_caracteres_especiais - num_numeros - num_maiusculas))
    
    senha_embaralhada = ''.join(random.sample(senha, len(senha)))
    
    return senha_embaralhada

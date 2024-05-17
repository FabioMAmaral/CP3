import itertools
import string

def ataque_bruteforce(senha):
    caracteres = string.printable.strip()
    tentativas = 0
    for comprimento in range(1, len(senha) + 1):
        for palpite in itertools.product(caracteres, repeat=comprimento):
            tentativas += 1
            palpite = ''.join(palpite)
            if palpite == senha:
                return (tentativas, palpite)
    return (tentativas, None)

senha = input("Digite a senha para quebrar: ")
tentativas, palpite = ataque_bruteforce(senha)
if palpite:
    print(f"Senha quebrada em {tentativas} tentativas. A senha é {palpite}.")
else:
    print(f"Senha não quebrada após {tentativas} tentativas.")

def validar_senha(senha, min_caracteres=8, min_especiais=1, min_numeros=1, min_maiusculas=1):
    pontos = 0
    
    if len(senha) >= min_caracteres:
        pontos += 1

    especiais = [c for c in senha if c in "!@#$%^&*()_+{}[]|\:;'<>?,./"]
    if len(especiais) >= min_especiais:
        pontos += 1
    
    numeros = [c for c in senha if c.isdigit()]
    if len(numeros) >= min_numeros:
        pontos += 1
    
    maiusculas = [c for c in senha if c.isupper()]
    if len(maiusculas) >= min_maiusculas:
        pontos += 1
    
    return pontos >= 4

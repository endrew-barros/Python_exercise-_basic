def sao_anagramas(str1, str2):
    # Remover espaços em branco e tornar todas as letras minúsculas para ignorar maiúsculas/minúsculas
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    # Verificar se as strings têm o mesmo comprimento
    if len(str1) != len(str2):
        return False

    # Usar um dicionário para contar a frequência de cada caractere em ambas as strings
    contagem1 = {}
    contagem2 = {}

    for letra in str1:
        if letra in contagem1:
            contagem1[letra] += 1
        else:
            contagem1[letra] = 1

    for letra in str2:
        if letra in contagem2:
            contagem2[letra] += 1
        else:
            contagem2[letra] = 1

    # Verificar se as contagens são iguais para todas as letras
    return contagem1 == contagem2

# Exemplo de uso
string1 = "Listen s"
string2 = "Silent s"

if sao_anagramas(string1, string2):
    print(f"'{string1}' e '{string2}' são anagramas.")
else:
    print(f"'{string1}' e '{string2}' não são anagramas.")

# Função para ler uma matriz de tamanho m x n
from email import header


def ler_matriz(m, n):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            elemento = float(input(f"Digite o elemento da posição ({i+1}, {j+1}): "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

# Função para somar duas matrizes
def somar_matrizes(matriz1, matriz2):
    m = len(matriz1)
    n = len(matriz1[0])
    resultado = []
    for i in range(m):
        linha = []
        for j in range(n):
            soma = matriz1[i][j] + matriz2[i][j]
            linha.append(soma)
        resultado.append(linha)
    return resultado

# Ler o tamanho das matrizes
m = int(input("Digite o número de linhas das matrizes: "))
n = int(input("Digite o número de colunas das matrizes: "))

# Ler as duas matrizes
print("Digite a primeira matriz:")
matriz1 = ler_matriz(m, n)

print("Digite a segunda matriz:")
matriz2 = ler_matriz(m, n)

# Somar as duas matrizes
resultado = somar_matrizes(matriz1, matriz2)

# Exibir a matriz resultante (soma)
print("A matriz resultante (soma) é:")
# for linha in resultado:
#     print(linha)
head(resultado)
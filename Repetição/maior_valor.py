lista_numeros = [10, 22, 25, 40, 25, 30]
maior_valor = lista_numeros[0]

for n in lista_numeros:
    if n > maior_valor:
        maior_valor = n

print(f"maior valor: {maior_valor}")

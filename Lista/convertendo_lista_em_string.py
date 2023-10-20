#declarando as variaveis
lista = ['primeiro','segundo','terceiro']

# Transformando em string uma lista
string1 = ', '.join(lista)
string2 = ' '.join(map(str, lista))

#Visualização dos resultados
print(type(lista))
print(type(string1))
print(type(string2))

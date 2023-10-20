# Como representar 3 notas para 5 alunos:
notas = [[7.5, 8.0, 6.0],
         [6.5, 5.8, 9.0],
         [4.5, 8.5, 7.0],
         [3.5, 8.0, 6.5],
         [2.5, 9.5, 5.7]]
print("\nImpressão sem formatação")
print(notas)
print("\n\nImpressão com formatação")
for line in notas:
    print ('  '.join(map(str, line))) #impressão com a transformação da matriz em string
    #print(line) # >>>> impressão com os colchetes
print("\n\nPara não perder o costume de fazer em uma linha")
print('\n'.join( [''.join( ['{:5}'.format(item) for item in row] ) for row in notas]) )
# explique como funcionam essas impressões

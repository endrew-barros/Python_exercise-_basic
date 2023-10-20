provedor = ['outlook.com','gmail.com']

while True:
    continuar =(input('Digite s  para sair: '))
    if continuar =='s':
        break
    email = input('Digite um email: ').split('@')
    print(email)
    if email[1] in provedor:
        print('o email é valido!!!')

    else:
        print('O email não é valido')
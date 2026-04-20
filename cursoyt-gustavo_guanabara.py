# print('ola mundo BR')

# 001ex
# nome=input('Com que estou falando: ')
# print(f'Muito prazer {nome}, seja bem vindo, vamos nos dar muito bem.') # v1 - com f-string
# print('Muito prazer {}, seja bem vindo, vamos nos dar muito bem.'.format(nome)) # v2 - format

# 002ex
# n1=int(input('Digite um numero para somar: ')) # v1 - sem o INT , o programa tava concatenando em vez de somar
# n2=int(input('Digite segundo numero: '))
#
# soma=(n1+n2)
# # print(type(soma)) # type mostra a class da variavel selecionada
# # print('A soma dos valores',n1,'e',n2, 'é: ',soma)
# # print(f'A soma dos valores {n1} e {n2}, é: {soma}')
# print('A soma dos valores {} e {}, é: {}'.format(n1,n2,soma))

# 003ex
teste=input('Digite algo: ')
print(teste.isdecimal())

# print('ola mundo BR')
# print('Parabens nova branch criada pc-servico')
#
# n1,n2=map(int,input('Digite 2 valores separado por espaço "A B", para Somar: ').split())
#
# soma=n1+n2
#
# print('A soma entre {} e {} vale {}'.format(n1,n2,soma))

# 004ex
#
# algo=input('Digite algo: ')
#
# print('O tipo primitivo desse valor é = ',type(algo))
# print('É somente espaços: {}'.format(algo.isspace())) # usando .format
# print('É um numero: ',algo.isnumeric())
# print('É alfabetico: ',algo.isalpha())
# print('É alfanumerico: ',algo.isalnum())
# print('Esta em maiusculo: ',algo.isupper())
# print('Esta em minusculo: ',algo.islower())
# print('Esta Capitalizado: ',algo.istitle())

# 003ex

# n1=int(input('Digite sua primeira nota: '))
# n2=int(input('Digite sua segunda nota: '))
# soma=n1+n2
# print('A soma dos valores {} e {} = {}'.format(n1,n2,soma))

# 005ex
# Ordem de precedencia 1-- (); 2-- **; 3-- *,/,//,%; 4-- +,-

# print(5+2)
# print(5-2)
# print(5*2)
# print(5/2)
# print(5**2)
# print(5//2)
# print(5%2)

# print(5+3*2) # testando ordens
# print(3*5+4**2)
# print(3*(5+4)**2)

# nome=input('Qual é seu nome?: ')
# print('Prazer em te conhecer {:~^20}!'.format(nome)) # teste de tipos de inferencia

# ???ex-Beecrowd - Ordenação
#
# a, b, c = map(int, input().split())
#
# ordenados = sorted([a, b, c])
#
# for n in ordenados:
#     print(n)
#
# print(a)
# print(b)
# print(c)
'''
Fluxo real:

[a, b, c] → cria lista
sorted(...) → ordena → [x, y, z]
* → vira → print(x, y, z)
sep='\n' → imprime cada valor em linha separada
'''
# a, b, c = map(int, input().split())
#
# print(*sorted([a, b, c]), sep='\n')
# print() # somente para ter 1 espaço em branco entre os resultado
# print(a, b, c, sep='\n')

# 006ex
# n1=int(input('Um valor: '))
# n2=int(input('Outro valor: '))
# soma=n1+n2
# mult=n1*n2
# div=n1/n2
# divInt=n1//n2
# exp=n1**n2
# print('A soma é {}, o produto é {} \ne a divisão é {:.2f}'.format(soma,mult,div),end=' ')
# print('e a Divisão Inteira é {} e a potencia é {}'.format(divInt,exp))




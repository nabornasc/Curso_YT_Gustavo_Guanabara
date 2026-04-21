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

# # 005desafio
# num=int(input('Digite um numero inteiro: '))
# sucessor=num+1
# antecessor=num-1
# print('O numero digitado foi {}, seu sucessor é {} e o antecessor é {}'.format(num,sucessor,antecessor))

# # 006desafio
# num=int(input('Digite um numero inteiro:'))
# dobro=num*2
# triplo=num*3
# raiz=num**(1/2)
# print('O numero digitado foi {:~^10}, e seu dobro é {:~^10}\nseu Triplo é {:~^10} e a sua Raiz Quadrada {:~^10.2f}'.format(num,dobro,triplo,raiz))

# # 007desafio
# nota1=float(input('Digite a 1 nota: '))
# nota2=float(input('Digite a 2 nota: '))
# media=(nota1+nota2)/2
# print('A media do aluno foi {:~^10.2f}'.format(media))

# # 008desafio
# metros=float(input('Quantos metros deseja converter? '))
# centimetros=metros*100
# milimetros=metros*1000
# print('{:~^15,.2f} metros, convertido é {:~^15,.2f} centimetros e {:~^15,.2f} milimetros'.format(metros,centimetros,milimetros).replace(',','X').replace('.',',').replace('X','.'))

# # 009 desafio -- PRIMEIRO CODIGO DE CABEÇA SEM REVISAR NA INTERNET OU IA =]]]]]]
# num=int(input('Digite um numero: '))
# mult=[1,2,3,4,5,6,7,8,9,10,11]
#
# for c in mult:
#     print(f'{num} x {c} = {num*c}')

# 010 desafio
# dinheiro=float(input('Digite o valor do dinheiro: '))
# dolar=float(input('Digite o valor do dolar: '))
# conversao=dinheiro/dolar
# print('Com R$ {:^10,.2f} , voce tera $ {:^10,.2f} dolar ao preço de: {:^10,.2f}.'.format(dinheiro,conversao,dolar))

# 011 dessafio
# largura=float(input('Digite a Largura da parede em Mts: '))
# altura=float(input('Digite a Altura da parede em Mts: '))
# quantM2=float(input('Qual rendimento da tinta em M²: '))
# metrosQuad=largura*altura
# areaPintada=metrosQuad/quantM2
# print('Para uma parede {} por {}, da um total de {}m². Que usará {}Litros com {}m² rendimento'.format(largura,altura,metrosQuad,areaPintada,quantM2))
#
# v2 - sugestao cloude
# Desafio 011 - Cálculo de tinta
# largura = float(input('Digite a Largura da parede em Mts: '))
# altura = float(input('Digite a Altura da parede em Mts: '))
# litrosTinta = float(input('Quantos litros de tinta da embalagem: '))
# rendTinta = float(input('Quantos m²/embalagem faz: '))
#
# rendEmba=litrosTinta/rendTinta
# metrosQuad = largura * altura
# areaPintada = metrosQuad / rendEmba
#
# print(f'\nPara uma parede de {largura}m x {altura}m:')
# print(f'  Área total:       {metrosQuad:.2f} m²')
# print(f'  Tinta necessária: {areaPintada:.2f} Litros')
# print(f'  Rendimento:       {rendEmba} m²/L')

# 012 desasfio
# preco=float(input('Digite um Preço: '))
# desconto=float(input('Digite o Desconto: '))
# novoPreco=preco*(1-desconto/100)
# print(f'O novo preço de {preco:.2f}, com desconto {desconto:.2f} é: {novoPreco:.2f}')

# 013 desafio
salario=float(input('Digite seu salario: '))
aumento=float(input('Digite aumento %: '))
novoSalario=salario*(1+aumento/100)
print(f'Seu novo salario é: R${novoSalario:.2f}')
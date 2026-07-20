'''
tempo=int(input('Quantos anos tem seu carro: '))

if tempo<=3: # somente IF é uma condição simples
    print('Carro novo')
else: # com ELSE se torna uma condição composta
    print('Carro velho')


print('carro novo' if tempo<=3 else 'carro velho') # IF SIMPLIFICADO possibilita fazer um teste em 1 linha

print('FIM')
'''
from os import system

# =======================================================
'''
nome = str(input('Digite seu nome: ')).title().strip()
print('Que nome lindo voce tem, {}'.format(nome) if nome=='Nabor' else 'Bom dia {}'.format(nome))
'''
# =======================================================
'''
n1=float(input('Digite Nota 1: '))
n2=float(input('Digite Nota 2: '))
med=(n1+n2)/2
print('Sua media foi: {:.2f}'.format(med))
print('Sua media foi boa! Parabens...' if med>=6 else 'Sua media foi ruim! Estude mais...') 
'''
# =======================================================
# desafio 28
'''
from random import randint
import os

def cls():
    try:
        os.system('cls' if os.name=='nt' else 'clear')
    except Exception:
        pass

while True:
    ale=randint(1,10)
    cls()
    num=int(input('Digite um numero de 1 a 10 [Sair=0]: '))
    if num==0:
        break
    print('Voce VENCEU! {} = {}'.format(ale,num) if ale==num else 'Voce PERDEU! {} = {} - Tente denovo'.format(ale,num))
'''
# =======================================================
# desafio 29
#
# vel=float(input('Digite sua velocidade: '))
# max=80
# vlrM=7
# if vel>max:
#     dif=vel-max
#     mul=dif*vlrM
#     print('A multa a pagar andar acima {}km/h é de R$ {:.2f}'.format(max,mul))

# =======================================================
# desafio 30
'''
num=int(input('Digite um numero: '))
print('{} é PAR!'.format(num) if num%2==0 else '{} é IMPAR!'.format(num))
'''
# =======================================================
# desafio 31
'''
dKm=int(input('Digite em Km a distancia da viajem: '))
tax1=.5
tax2=.45
psg=dKm*tax1 if dKm<200 else dKm*tax2
print('Sua passagem deu R${:.2f}'.format(psg))
'''
# =======================================================
# desafio 32
'''
ano=int(input('Digite o ano qualquer: '))
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('Analisando o ano de {} é BISSEXTO'.format(ano))
else:
    print('Analisando o ano de {} não é BISSEXTO'.format(ano))
'''
# =======================================================
# desafio 33
'''
list_num=[]
for cont in range (3):
    list_num.append(int(input('Digite um numero: ')))
    """ # v1 usando lista e modulos, tamanho dinâmico. 
    menor=min(list_num)
    maior=max(list_num)
    """
a=list_num[0] # v2 usando variáveis fixas, seguindo o exercício
b=list_num[1]
c=list_num[2]

if a>=b and a>=c:
    maior = a
    menor = b if b<=c else c
elif b>=a and b>=c:
    maior = b
    menor = a if a<=c else c
else:
    maior = c
    menor = a if a<=b else b

print('O menor numero: {}\nO maior numero: {}'.format(menor,maior))
'''
# =======================================================
# desafio 34
'''
sal=float(input('Digite seu salario: '))
cort=1250
tax1=.1
tax2=.15
print('Seu novo salário é: R${:.2f}'.format(sal+sal*tax2) if sal<cort else sal+sal*tax1)
'''
# =======================================================
# desafio 35
med=[]
med2=[]
for cont in range (3):
    med.append(int(input(f'Digite o tamanho do {cont+1} segmento: ')))

for cont2 in range(len(med)):
    for cont3 in range(cont2+1,len(med)):
        if med[cont2]<med[cont3]:
            med2.append(med[cont2])

if min(med2)+max(med2)>max(med):
    print(f'Os numero {med} podem formar um Triangulo')
else:
    print(f'Os numero {med} não podem formar um Triangulo')
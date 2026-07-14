'''
from math import trunc

num=float(input("digite um numero: "))
print('O Numero digitado foi {}, e sua porção inteira é {}'.format(num,trunc(num)))
'''
'''
import math
from math import tan, cos, sin, radians


num=float(input('Digite um numero: '))
print('O Numero digitado {}, e sua parte inteira é {}'.format(num,int(num)))
'''
'''
from math import hypot

co=float(input('Digite o cateto oposto: '))
ca=float(input('Digite o cateto adjacente: '))

# hi=(co**2+ca**2)**(1/2)
hi=hypot(co,ca)

print('A hipotenusa do CO {} e CA {} é {:.2f} '.format(co,ca,hi))
'''
'''
from math import radians, sin, cos, tan

ang=float(input('Digite o angulo do triangulo: '))

sen= sin(radians(ang))
cos= cos(radians(ang))
tan= tan(radians(ang))

print('O angulo de {:.1f}º em RAD {:.3f} tem:\n Seno = {:.3f}\n Cosseno = {:.3f}\n Tangente = {:.3f}'.format(ang,radians(ang),sen,cos,tan))
'''
'''
from random import choice # choice - função para escolher aleatorio

lista_alunos=[]

for c in range(3):
    lista_alunos.append(str(input('Digite o nome do aluno: ')))

escolhido=choice(lista_alunos)

print('O aluno escolhido foi {}'.format(escolhido))
'''
'''
from random import shuffle

alunos=[]

for cont in range(4):
    alunos.append(str(input('Digite o nome do aluno:')))

# random.shuffle(alunos)
shuffle(alunos)

print(alunos)
'''
'''
from pygame import init, mixer

init()
mixer.music.load('music/CPM22_1min.mp3')
mixer.music.play()

while mixer.music.get_busy():
    pass
'''
# =================================================================
'''
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiusculo: {nome.upper()}')
print(f'Seu nome em minusculo: {nome.lower()}')
print(f'Seu nome completo tem {len(nome)-nome.count(' ')} letras')
print(f'Seu primeiro nome tem {nome.find(' ')} letras') # este metodo retornar o valor do primeiro espaço encontrado, assim resultando no mesmo valor do primeiro nome ' sem usar o len '
list=nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(list[0],len(list[0])))
'''
'''
cid=str(input('Digite o nome da sua cidade: ')).strip()

print(cid[:5].lower() == 'santo')
'''
'''
nome=str(input('Digite seu nome completo: ')).lower().strip()

print(f'Seu nome contem SILVA: {"silva" in nome}')
'''
'''
frs=str(input('Digite uma frase: ')).lower().strip()

print(f'Quantas letras "A" apareceu na frase: {frs.count("a")} und')
print(f'A primeira letra "A" apareceu na posição: {frs.find("a")+1}')
print(f'A ultima letra "A" apareceu na posição: {frs.rfind("a")+1}')
'''
'''
nome=str(input('Digite seu nome completo: ')).lower().strip().split()

print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu ultimo nome: {nome[len(nome)-1]}')
'''
# ================================================================
#
# from random import randint
# from time import sleep
#
# numSorteado=randint(1,5)
# print('-=-' * 20)
# print('Tente adivinhar o numero que escolhi [0 a 5]...')
# print('-=-' * 20)
# jogador=int(input('Em que numero eu pensei?: '))
# print('PROCESSANDO...')
# sleep(1)
# print('Parabens! Voce venceu...' if numSorteado==jogador else 'Que pena! Voce perdeu...\n\n Tente novamente')

# ================================================================

# velCarro=float(input('Qual a velocidade do carro: '))
# if velCarro<80:
#     print('Tenha um bom dia, diriga com segurança.')
# else:
#     multa=(velCarro-80)*7
#     print('MULTADO! Você excedeu o limite de velocidade.\n Valor da Multa: R${:.2f}'.format(multa))

# ================================================================

# num=int(input('Digite um numero inteiro: '))
# result=num%2
# print('O numero {} é PAR'.format(num) if result==0 else 'O numero {} é IMPAR'.format(num))

# ================================================================

# dist=float(input('Qual a distancia da sua viagem: '))
# print('='*30)
# preco= dist*0.5 if dist<=200 else dist*0.45
# print('O preço da sua passagem é R${:.2f}'.format(preco))

# ================================================================
# from datetime import date
#
# ano=int(input('Que ano quer analisar: '))
#
# if ano==0:
#     ano=date.today().year
#
# if ano%4==0 and ano%100!=0 or ano%400==0:
#     print('O ano de {} é BISSEXTO'.format(ano))
# else:
#     print('O ano de {} não é BISSEXTO'.format(ano))

# ================================================================

# nums=[]
# for cont in range(3):
#     nums.append(int(input(f'Digite o {cont+1} numero: ')))
#
# print(f'O menor é {min(nums)}\nO maior é {max(nums)}')

# ================================================================

sal=float(input('Digite seu salario: '))
print(f'Baseado em \033[33m{sal:.2f}\033[m reais.\n Seu novo salario é de \033[32m{sal+sal*.15 if sal<=1250 else sal+sal*.10}')

# ================================================================

# segm=[]
# for cont in range(3):
#     segm.append(int(input('Digite o {} do segmento: '.format(cont+1))))
#
# if (segm[0] < segm[1] + segm[2] and
#     segm[1] < segm[0] + segm[2] and
#     segm[2] < segm[0] + segm[1]):
#     print('Os segmentos acima PODEM FORMAR um triangulo')
# else:
#     print('Os segmentos acima NÃO PODEM FORMAR um triangulo')









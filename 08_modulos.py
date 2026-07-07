# floor retorna somente o numero inteiro
# sqrt retorna raiz quadrada

import math
import random


# num=int(input('DIgite um numero: '))
# raiz=sqrt(num)
# print(f'A raiz de {num} é igual a {floor(raiz):.2f}')

# ===========================================

# desafio 16

# num=float(input('Digite um numero REAL: '))
# print(f'A parte inteira do {num} é {floor(num)}')

# desafio 17
#
# ctO=int(input('Digite o Cateto oposto: '))
# ctA=int(input('Digite o Cateto adjacente: '))
# hiP=hypot(ctO,ctA)
# hip=sqrt(ctO**2+ctA**2) # O calculo da hipotenusa vem do Oposto*2 + Adjacente*2 - RaizQuad.
# print(f'O Cateto oposto {ctO}, e Cateto adjacente {ctA} é igual a Hipotenusa de {hiP:.2f} // {hip:.2f}')

# desafio 18

# anG=int(input('Digite um Angulo: '))
#
# seno=math.sin(math.radians(anG))
# cosseno=math.cos(math.radians(anG))
# tangente=math.tan(math.radians(anG))
#
# print(f'O angulo {anG}º,\n tem Seno de: {seno:.3f},\n Cosseno de: {cosseno:.3f},\n Tangente de: {tangente:.3f}')

# desafio 19 e 20

alunos=[]

for cont in range(3):
    alunos.append(input("Digite o nome do aluno: "))

# ordem_sorteada=random.sample(alunos,len(alunos)) # sample - permite sortear aleatoriamente sem repetir posição
posicoes = list(range(len(alunos)))
random.shuffle(posicoes)

sorteio = list(zip(posicoes, alunos))
sorteio.sort(key=lambda x: x[0])

# print(f'Lista de Alunos: {alunos}')
# print(f'Lista de Ordem Sorteada: {ordem_sorteada}')

for posicao,aluno in sorteio:
    print(f'{posicao+1} - {aluno}')

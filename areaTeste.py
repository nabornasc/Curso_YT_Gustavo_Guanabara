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

from pygame import init, mixer

init()
mixer.music.load('music/CPM22_1min.mp3')
mixer.music.play()

while mixer.music.get_busy():
    pass





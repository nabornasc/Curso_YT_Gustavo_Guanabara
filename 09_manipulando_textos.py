frase="Curso em video Python"

# fatiamento de strings Inicio:Fim:Pulos
print(frase[6:14:1])
print(frase[9::3])

# analises
print(len(frase)) # Contagem total
print(frase.count('o')) # contagem especifica
print(frase.count('o',0,13)) # contagem especifica c/fatiamento
print(frase.find('deo')) # encontrar frase - monstrando aonde começa "11"
print(frase.find('Android')) # a busca retorna -1 "não encontrado"
print('Curso' in frase) # retorna bool , confirmando se achou frase na variavel ou vetor

# Transformação
print(frase.replace('Python','Android')) # Troca frase dentro da variavel ou vetor
print(frase.upper()) # metodo precisa () para funcionar " transforma em Maiusculo"
print(frase.lower()) # transforma em Minusculo
print(frase.capitalize()) # Somente 1º Letra Maiuscula
print(frase.title()) # transforma palavras por palavra em 1º Maiuscula

frase2 = '    Aprenda Python   '
print(frase2.strip()) # remove espaço inuteis inicio/fim
print(frase2.rstrip()) # remove somente espaços no fim
print(frase2.lstrip()) # remove somente espaços no inicio

# Divisão
print(frase.split()) # Cria divisão entre as palavras, gerando uma lista de palavras, apartir de uma frase.

# Junção
test=frase.split()
print('_'.join(test)) # Uniao de lista de palavras, em um frase. dentro das aspas pode adicionar a formatação
print('-'.join(frase.split())) # Uniao aplicado com split, para alterar caractere entre palavras

# ==================================================

frase3=("""
    Durante o fim de semana Nabor decidiu organizar sua garagem enquanto ouvia música e 
    pensava em como seria bom terminar logo os exercícios de Python para poder assistir um 
    filme tranquilo depois do jantar com a família reunida na sala principal da casa.
    """)

# uma str é imutavel.

# ==================================================
# desafio 22
'''
nome=str(input('\nDigite seu Nome Completo: ').strip())

print(f'Maiuscula - {nome.upper()}')
print(f'Minuscula - {nome.lower()}')
print(f'Contagem Total s/espaços - {len(''.join(nome.split()))} letras')
print(f'Contagem do 1º Nome - {len(nome.split()[0])} letras')
'''
# ==================================================
#  desafio 23
'''
casaDec=['milhar','centena','dezena','unidade']
num=int(input('Digite um numero inteiro[xxxx]: '))
for cont in range(3,-1,-1):
    print(f'{casaDec[cont].title()}: {str(num)[cont]}')
'''
# ====================================================
# desafio 24
'''
cid=str(input('Digite o nome da sua Cidade: ')).upper().split()

if cid[0]=='SANTO':
    print(f'Sua cidade começa com {cid[0]}')
else:
    print(f'Sua cidade não começa com "SANTO"')
'''

# ====================================================
# desafio 25
#
# nome=str(input('Digite seu nome Completo: ')).upper().split()
#
# flag=True
#
# for nome2 in nome:
#     if nome2=='SILVA':
#         print(f'Em seu nome tem {nome2}')
#         flag=False
#
# if flag:
#     print(f'Em seu nome não contem "SILVA"')

# ====================================================
# desafio 26
#
# frase4=str(input('Digite uma frase: ')).strip()
# print(f'{frase4.count('A')} - "A" Maiusculo') # procura letra Maiuscula
# print(f'{frase4.count('a')} - "a" Minusculo') # procura letra Minuscula
# print(f'1ºvez encontrado "A/a" na posição - {frase4.lower().find('a')}')
# print(f'Ultima vez encontrado "a" na posição - {frase4.lower().rfind('a')}')

# ====================================================
# desafio 27

nome=str(input('Digite seu nome Completo: ')).title().split()
print(f'Primeiro nome: {nome[0]}\nÚltimo nome: {nome[len(nome)-1]}')







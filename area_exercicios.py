# desafio 37

# from os import system, name
#
# cls=lambda:system('cls' if name == 'nt' else 'clear')
#
# num=int(input('Digite um numero inteiro: '))
# cls()
#
# opc=int(input(f'1 - binario\n2 - octal\n3 - hexadecimal\nEscolha uma opção: '))
# cls()
#
# if opc==1:
#     binario=bin(num)[2:]
#     print(binario)
# elif opc==2:
#     octal=oct(num)[2:]
#     print(octal)
# elif opc==3:
#     hexadec=hex(num)[2:]
#     print(hexadec)

# ===========
# desafio 38
# ===========

# n1=int(input('Digite 1º numero: '))
# n2=int(input('Digite 2º numero: '))
#
# if n1>n2:
#     print(f'{n1} é maior que {n2}')
# elif n1<n2:
#     print(f'{n1} é menor que {n2}')
# else:
#     print(f'Não exite maior, pois {n1} e {n2} são iguais!')

# ===========
# desafio 39
# ===========

from datetime import datetime

anoAtual=datetime.today().year
anoDig=int(input('Digite o ano de nascimento: '))

if anoAtual-18 < anoDig:
    print(f'Ainda vai se alistar, faltam {(anoDig-anoAtual)+18} anos')

elif anoAtual-18 >= anoDig and anoAtual-45 <= anoDig:
    print('Hora de se alistar' if anoAtual-18 <= anoDig else
          f'Passou {(anoAtual-anoDig)-18} anos do prazo de alistamento, limite 45 anos.')
else:
    print('Passou do prazo de alistamento')

# ===========
# desafio 40
# ===========







# ===========
# desafio 41
# ===========


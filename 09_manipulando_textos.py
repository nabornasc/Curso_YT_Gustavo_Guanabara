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



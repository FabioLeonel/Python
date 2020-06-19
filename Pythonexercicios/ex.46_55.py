#ex.46
from time import sleep
print('Os fogos vão começar em...')
for fire in range(10, 0, -1):
    print(fire)
    sleep(1)
print('FOGGGOOOOO!!!!')

#ex.47
for pares in range(2, 51, 2):
    print(pares)

#ex.48
soma = 0
conta = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        conta += 1
        soma += c
print(f'A soma de todos os {conta} é {soma}')

#ex.49
number = int(input('Tabuada do '))
print('='*10)
for cont in range(1, 11):
    print(f'{number} x {cont:2} = {cont*number}')

#ex.50
soma1 = 0
pares = 0
for c1 in range(1, 7):
    somas = int(input('numero: '))
    if somas % 2 == 0:
        soma1 += somas
        pares += 1
if pares != 0:
    print(f'São: {pares} pares e a soma é {soma1}')
else:
    print('Não foram escolhidos numeros pares')

#ex.51
termo = int(input('Escolha o primeiro termo da PA: '))
razao = int(input('Escolha a razão: '))
n = int(input('Quantos exibir: '))
ultimo = termo + (n-1)*razao  #a = a1+(n-1)*razão
ultimo += 1
for pa in range(termo, ultimo, razao):
    print(pa, end=' ')

#ex.52 pt.1
pr = int(input('Escolha um numero: '))
mult = 0
for pri in range(2, pr):
    if pr % pri == 0:
        print(f'Multiplo de {pri}')
        mult += 1
if mult == 2:
    print(f'{pr} é primo')
else:
    print(f'{pr} não é primo')

#   pt.2
pr = int(input('numero: '))
mult = 0
for pri in range(1, pr + 1):
    if pr % pri == 0:
        print(f'\033[33m', end='')
        tot += 1
    else:
        print(f'\033[31m', end='')
    print(f'{pri}', end='')
print(f'O numero {pr} foi divisivel {mult} vezes')
if mult == 2:
    print('É primo')
else:
    print('Não é primo')

#ex.53  pt.1
palind = str(input('Crie uma frase: ')).strip()
palind = palind.replace(' ', '').lower()
for line in palind:
    reverso = palind[::-1]
if palind == reverso:
    print(f'A frase é um palíndromo')
else:
    print('Não é um palíndromo')

#   pt.2
palind = str(input('Crie uma frase: ')).strip()
palavras = palind.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if palind == inverso:
    print(f'A frase é um palíndromo')
else:
    print('Não é um palíndromo')

#ex.54
from datetime import date
count1 = 0
count2 = 0
for ano in range(1, 8):
    ano = int(input('Em que ano você nasceu?'))
    a = date.today().year - ano
    if a >= 21:
        count1 += 1
    else:
        count2 += 1
print(f'{count1} pessoas ja atingiram a maioridade e {count2} ainda não atingiram')

#ex.55
lista = []
for peso in range(1, 6):
    p = float(input('Qual o seu peso? '))
    lista.append(p)
print(f'O maior peso é {max(lista)} e o menor peso é {min(lista)}')

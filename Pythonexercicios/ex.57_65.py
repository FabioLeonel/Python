#AULA 14
# ex.57
sexo = input('Qual o seu sexo? [M/F]').strip().lower()[0]
while sexo not in 'mf':
    sexo = input('Digite um valor válido [M/F]').strip().lower()[0]
print(f'Você escolheu \033[31m{sexo.upper()}\033[m')

# ex.58 pt.1
from random import randint
print('O computador escolheu um numero entre 0 e 10')
num = randint(0, 10)
resp = 0
while resp != num:
    resp = int(input('Digite um valor:'))
    if resp != num:
        resp += 1
        print('Tente novamente')
print(f'Parabens, o computador escolheu {num} e você precisou de {resp} tentativas')

#   pt.2
from random import randint
print('O computador escolheu um numero de 0 a 10...')
computador = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Escolha um numero: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente de novo')
        elif jogador > computador:
            print('Menos... tente de novo')
print(f'Acertou com {palpites} tentativas')

# ex.59
v1 = int(input('Digite o 1° valor: '))
v2 = int(input('Digite o 2° valor: '))
menu = 0
while menu != 5:
    menu = int(input('''
    O que você quer fazer?:
    ---------------------------
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa
    ---------------------------'''))
    if menu == 1:
        print(f'---> {v1}+{v2}= {v1 + v2}')
    elif menu == 2:
        print(f'---> {v1}x{v2}= {v1 * v2}')
    elif menu == 3:
        if v1 > v2:
            print(f'---> {v1}>{v2}')
        elif v1 < v2:
            print(f'---> {v2}>{v1}')
        else:
            print(f'---> {v1} = {v2}')
    elif menu == 4:
        v1 = int(input('1° numero: '))
        v2 = int(input('2° numero: '))
    elif menu == 5:
        print('Finalizando...')
    else:
        print('Coloque um valor valido')

# ex.60 pt1.
fa = int(input('Escolha um numero para fatorar: '))
f1 = fa
fato = 1
while fa != 1:
    fato *= fa
    fa -= 1
    print(fa, fato)
print(f'{f1}!= {fato}')

#   pt.2
fa = int(input('fatorial:'))
for r in range(1, fa):
    fa = r * fa
print(fa)

#   pt.3
from math import factorial
n = int(input('Fatorial: '))
c = n
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    c -= 1
print(factorial(n))

# ex.61
n1 = int(input('Primeiro termo da PA: '))
r1 = int(input('Razão da PA: '))
p1 = 0
while p1 != 10:
    print(n1, end=' ')
    n1 += r1
    p1 += 1

# ex.62
n2 = int(input('Primeiro termo da PA: '))
r2 = int(input('Razão da PA: '))
p2 = 0
p4 = 10
while p2 != p4:
    print(n2, end=' ')
    n2 += r2
    p2 += 1
    if p2 == 10:
        p3 = int(input('\nQuantos termos a mais? '))
        if p3 == 0:
            print('<---Fim')
            break
        else:
            p4 += p3
            p2 -= p3

#   pt.2
n2 = int(input('Primeiro termo da PA: '))
r2 = int(input('Razão da PA: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{n2} ', end='')
        n2 += r2
        cont += 1
    mais = int(input('\nQuantos a mais? '))
    print('<---Fim')

# ex.63
n4 = int(input('Quantos termos? '))  #1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
n3 = 0
fi = 1
cont = 0
print('A sequencia de Fibonacci é:\n')
while cont != n4:
    print(n3, end=' ')
    n3 = (fi - n3)
    fi = fi + n3
    cont += 1
print('-Fim')

# ex.64
num1 = varia = cont2 = 0
while varia != 999:
    varia = int(input('Digite um numero (999 para parar): '))
    if varia == 999:
        print(f'Foram somados {cont2} valores, e a soma deles é {num1}')
    num1 += varia
    cont2 += 1
print(f'--Fim--')

# ex.65
resp = ''
media = maior = menor = cont3 = n5 = 0
while resp != 'n':
    n5 = int(input('Escolha um numero: '))
    media += n5
    cont3 += 1
    if cont3 == 1:
        maior = menor = n5
    else:
        if n5 > maior:
            maior = n5
        if n5 < menor:
            menor = n5
    resp = input('Digite [n] para parar] ').lower().strip()[0]
print(f'A média dos valores foi {media / cont3}\nmaior valor: {maior}\nmenor valor: {menor}')

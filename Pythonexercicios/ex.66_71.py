# Aula 15
# ex.66
n = cont = soma = 0
while True:
    n = int(input('Digite um numero(999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitados {cont} numeros e a soma deles é {soma}')

# ex.67
print('-->Tabuada<--')
t = x = 1
while True:
    print('-' * 23)
    t = int(input('Tabuada de qual valor? [negativo para parar]'))
    print('-' * 23)
    if t < 1:
        break
    for x in range(1, 11):
        print(f'{t} x {x:2} = {t * x}')
print('Encerrada, volte sempre')

# ex.68
from random import randint
print('==' * 25, f'\nJogo do Par ou Impar\n{"==" * 25}')
pi = 'PpIi'
player = computador = resultado = vitoria = 0
while True:
    player = int(input('Escolha um valor: '))
    computador = randint(0, 10)
    resultado = computador + player
    if player in range(0, 11):
        pi = input('Par ou ímpar? [P/I]').lower()[0]
        while not pi in 'PpIi':
            pi = input('\033[31mcoloque "P" ou "I"\033[m').lower()[0]
        if pi in 'PpIi':
            print('--'*25)
            print(f'Você jogou {player} e o computador {computador}. Total de {player + computador}', end='')
            print(', DEU PAR' if resultado % 2 == 0 else ', DEU IMPAR')
            if pi == 'p':
                if resultado % 2 == 0:
                    vitoria += 1
                elif resultado % 2 != 0:
                    break
            if pi == 'i':
                if resultado % 2 == 0:
                    break
                elif resultado % 2 != 0:
                    vitoria += 1
    else:
        print('--' * 20)
        print('\033[31mColeque um numero entre 0 e 10\033[m')
        print('--' * 20)
print('--' * 25)
print(f'Game Over, você venceu {vitoria} vezes')

#ex.69
print('-------Ficha-------')
homens = mulheres = idades = continuar = 0
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        idades += 1
    sexo = ' '
    while sexo not in 'mf':
        sexo = input('Sexo: [M/F]').lower()[0]
    if sexo in 'mf':
        if sexo in 'm':
            homens += 1
        if sexo in 'f' and idade < 20:
            mulheres += 1
    print('-' * 20)
    continuar = ' '
    while continuar not in 'sn':
        continuar = input('Continuar? [S/N]').lower().strip()[0]
    if continuar == 'n':
        break
print('=' * 25)
print(f'{idades} tem mais de 18 anos, {homens} homens foram cadastrados e {mulheres} mulheres tem menos de 20 anos')

#ex.70
print('---$ Mercadinho $---')
preço = total = mil = barato1 = 0
produto = barato = ' '
while True:
    produto = input('Nome do Produto: ')
    preço = float(input('Preço do Produto: $'))
    if barato1 == 0 or preço <= barato1:
        barato1 = preço
        barato = produto
    total += preço
    if preço > 1000:
        mil += 1
    continuar = ' '
    while continuar not in 'sn':
        continuar = input('Outro Produto?[S/N] ').lower().strip()[0]
    if continuar == 'n':
        break
    continuar = '0'
print(f'O total a pagar é {total:.2f}$, {mil} produtos custam mais de 1000$')
print(f'O mais barato é {barato} que custa {barato1}$')
print('Volte Sempre')

#ex.71    pt.1
#{'blabla':^30} ^ para centralizar em 30 caracteres
print('=' * 25,f'\n{"BANCO 24hrs":^30}\n{"=" * 25}')
c50 = c20 = c10 = c01 = 0
saque = int(input('Valor do Saque: '))
resto = saque
while True:
    while resto - 50 >= 0:
        resto = resto - 50
        c50 += 1
    while resto - 20 >= 0:
        resto = resto - 20
        c20 += 1
    while resto - 10 >= 0:
        resto = resto - 10
        c10 += 1
    while resto - 1 >= 0:
        resto = resto - 1
        c01 += 1
    break
print(f'Para o saque de {saque}$ serão:')
if c50 > 0:
    print(f'{c50} notas de 50$')
if c20 > 0:
    print(f'{c20} notas de 20$')
if c10 > 0:
    print(f'{c10} notas de 10$')
if c01 > 0:
    print(f'{c01} notas de 1$')
print('=' * 25)

#ex.71   pt.2
valor = int(input('Saque: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} de {ced}$')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

#ex.71   pt 3 == forma matematica
valor = int(input("informe o valor a ser sacado : "))
nota50 = valor // 50
valor %=  50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor // 1
print(f"notas de 50 = {nota50}")
print(f"notas de 20 = {nota20}")
print(f"notas de 10 = {nota10}")
print(f"notas de 1 = {nota1}")

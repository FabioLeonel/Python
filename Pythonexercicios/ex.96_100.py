#AULA 20
#ex.96
def area(larg, comp):
    a = l * c
    print(f'A área de um terreno {larg} x {comp} é de {a}m²')


print('Controle de Terrenos')
l = float(input('Largura(m): '))
c = float(input('Comprimento (m): '))
area(l, c)

#ex.97
def escreva(ola):
    print(f'-' * (len(ola) + 2))
    print(f' {ola}')
    print(f'-' * (len(ola) + 2))


escreva('Olá. Mundo!')
escreva('Olá')

#ex.98
from time import sleep
def contator(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    if fim > inicio:
        while fim >= inicio:
            print(inicio, end=' ') #caso precise, usar o , flush=True / vai mudar o jeito que o sleep conta
            inicio += passo
            sleep(0.3)
    elif fim < inicio:
        while inicio >= fim:
            print(inicio, end=' ')
            if passo >= 0:
                inicio -= passo
                sleep(0.3)
                if inicio < fim:
                    break
    print()
    print('-' * 30)


print('=' * 30)
contator(1, 10, 1)
contator(10, -1, 2)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contator(i, f, p)

#ex.99
from time import sleep
def maior(*num):
    print('Analisando os valores...')
    sleep(1)
    for valores in num:
        print(valores, end=' ')
    print(f'Foram informados {len(num)} valores')
    if len(num) == 0:
        num += (0,)
    print(f'O maior valor é {max(num)}')
    print('-' * 35)
    sleep(1)


print('=' * 35)
maior(2, 9, 3, 5, 7, 1)
maior(4, 7, 0)
maior(6)
maior()

#ex.100
from random import randint
def sorteia(sort):
    print(f'Sorteando  valores da lista: ')
    for r in range(5):
        ran = randint(0, 10)
        sort.append(ran)
        print(ran, end=' ')
    print()


def somapar(soma):
    print(f'Somando os valores pares temos: ')
    som = 0
    for r in numeros:
        if r % 2 == 0:
            som += r
    print(som)


numeros = []
sorteia(numeros)
somapar(numeros)

#AULA 10
# ex. 28
from time import sleep
from random import randint
print('O computador escolheu um numero entre \033[31m0\033[m e \033[31m5\033[m')
num = randint(0, 5)
resposta = int(input('Qual numero é?\n'))
print('Processando...')
sleep(2)
if resposta == num:
    print(f'Parabens, a resposta  \033[31m{resposta}\033[m é igual a do computador')
else:
    print(f'O computador ganhou, a resposta era \033[31m{num}')

# ex. 29
vel = int(input('velocidade em km/h: '))
print('analizando a velocidade...')
if vel > 80:
    print(f'você foi multado em {(vel - 80) * 7} reais')
else:
    print(f'não houve multa')

# ex.30
import math
num1 = int(input('Escolha um numero: '))
if num1 % 2 == 0:
    print(f'O numero {num1} é par')
else:
    print(f'O numero {num1} é impar')

# ex.31 pt.1
via = int(input('Qual a distancia da viagem? '))
if via <=200:
    custo = via * 0.50
else:
    custo = via * 0.45
print(f'A viagem vai custar {custo:.2f}$')
#   pt2.
via = float(input('Qual a distancia?: '))
custo = via * 0.50 if via <= 200 else via * 0.45
print(f'O preço vai ser {custo}$')

# ex.32
from datetime import date
ano = int(input('escolha um ano: (0 para o ano atual)'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')

# ex.33 pt.1
n1 = int(input('primeiro: '))
n2 = int(input('segundo: '))
n3 = int(input('terceiro: '))
mai = n1
if n2 > mai:
    mai = n2
if n3 > mai:
    mai = n3
men = n1
if n2 < men:
    men = n2
if n3 < men:
    n3 = men
print(f'O maior é {mai} e o menor é {men}')

# pt2.
n1 = int(input('p: '))
n2 = int(input('s: '))
n3 = int(input('t: '))
lista = [n1, n2, n3]
print(f'Maior: {max(lista)}\n Menor: {min(lista)}')

# ex.34
salario = float(input('Qual seu salario?: '))
if salario > 1250.00:
    print(f'seu aumento foi de 10%: {salario * 10 / 100:.2f}')
else:
    salario <= 1250.00
    print(f'seu aumento foi de 15%: {salario * 15 / 100:.2f}')

# ex.35
r1 = float(input('reta 1: '))
r2 = float(input('reta 2: '))
r3 = float(input('reta 3: '))

if r2 - r3 < r1 < r2 + r3:
    r1 - r3 < r2 < r1 + r3
    r1 - r2 < r3 < r1 + r2
    print('è possivel montar um triangulo')
else:
    print('não é possivel montar um triangulo')

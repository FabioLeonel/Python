# Aula 18
#ex. 84
cadastro = []
pessoa = []
pesado = leve = 0
while True:
    n = input('Nome: ')
    p = float(input('Peso: '))
    pessoa.append(n), pessoa.append(p)
    cadastro.append(pessoa[:])
    if p >= pesado:
        pesado = p
    if leve == 0 or p <= leve:
        leve = p
    pessoa.clear()
    o = input('Continuar? [S/N]').lower()
    if 'n' in o:
        break
print(f'{len(cadastro)} pessoas foram cadastradas')
print(f'O maior peso foi de {pesado}kg. Peso de ', end='')
for v in cadastro:
    if v[1] == pesado:
        print(f'[{v[0]}] ', end='')
print(f'\nO menor peso foi de {leve}kg. Peso de ', end='')
for v in cadastro:
    if v[1] == leve:
        print(f'[{v[0]}] ', end='')

#ex.85
valores = [[], []]
for n in range(7):
    v = int(input(f'Digite o {n+1}° numero: '))
    if v % 2 == 0:
        valores[0].append(v)
    else:
        valores[1].append(v)
valores[0].sort()
valores[1].sort()
print(f'Os pares são: {valores[0]}')
print(f'Os impares são: {valores[1]}')

#ex.86
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite ujm valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}:^5]', end='')
    print()

#ex.87
matriz = [[], [], []]
pares = coluna = 0
for l in range(3):
    for c in range(3):
        matriz[l].append(int(input('Digite um valor: ')))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos pares é: {pares}')
for l in range(3):
    coluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {coluna}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')

#ex.88
from random import randint
from time import sleep
print('='*33)
print(f'{"JOGA NA MEGA SENA":^30}')
print('='*33)
megasena = []
jogo = []
resp = int(input(f'Quantos jogos serão gerados: '))
total = 1
while total <= resp:
    cont = 0
    while True:
        s = randint(1, 60)
        if s not in jogo:
            jogo.append(s)
            cont += 1
        if cont >= 6:
            break
    megasena.append(jogo[:])
    jogo.sort()
    total += 1
    jogo.clear()
for i, l in enumerate(megasena):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print(f'{"BOA SORTE!":-^33}')

#ex.89  pt.1
turma = []
aluno = []
notas = []
while True:
    n = input('Aluno: ')
    p1 = float(input('P1: '))
    p2 = float(input('P2: '))
    m = (p1 + p2) / 2
    aluno.append(n)
    notas.append(p1), notas.append(p2), notas.append(m)
    aluno.append(notas[:])
    notas.clear()
    turma.append(aluno[:])
    aluno.clear()
    resp = input('Outro aluno? [S/N]').lower()
    if 'n' in resp:
        break
print('='*30)
print('N°. NOME      MÉDIA')
print('-'*30)
for t, v in enumerate(turma):
    print(t, end='  ')
    print(v[0], end='  ')
    print(f'{v[1][2]}')
print('-'*30)
while True:
    a = int(input('Mostrar nota de qual aluno? (999 interrompe)'))
    if a == 999:
        break
    print(f'Notas de {turma[a][0]} são {turma[a][1][:2]}')
print('='*30)
print('FINALIZADO!')

#ex.89 pt2
turma = []
while True:
    n = input('Aluno: ')
    p1 = float(input('P1: '))
    p2 = float(input('P2: '))
    m = (p1 + p2) / 2
    turma.append([n, [p1, p2], m])
    resp = input('Outro aluno? [S/N]').lower()
    if 'n' in resp:
        break
print('='*30)
print(f'{"N°.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for t, v in enumerate(turma):
    print(f'{t:<4}{v[0]:<10}{v[2]:>8.1f}')
print('-'*30)
while True:
    a = int(input('Mostrar nota de qual aluno? (999 interrompe)'))
    if a == 999:
        break
    if a <= len(turma) - 1:
        print(f'Notas de {turma[a][0]} são {turma[a][1]}')
print('='*30)
print('FINALIZADO!')

#AULA 21
#ex. 106
def voto(ano):
    from datetime import date
    n = date.today().year - ano
    print(f'{n} anos: ', end='')
    if n < 16:
        print('Não vota')
    elif 16 <= n < 18 or n >= 65:
        print('Voto opcional')
    else:
        print('Voto obrigatório')


voto(int(input('Ano de Nascimento: ')))

#ex. 102
def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número
    show = True, mostra o calculo da fatorial
    show = False, não mostra o calculo da fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(int(input('Numero para fatorar: ')), True))
help(fatorial)

#ex. 103  pt.1
def ficha(nome='desconhecido', gol=0):
    print(f'O jogador {nome}, fez {gol} gols na partida')


jogador = input('Nome do Jogador: ')
gols = input('Gols na partida: ')
if gols.isnumeric():
    gols = int(gols)
else:
    g = 0
if jogador.strip() == '':
    ficha(gol=gols)
else:
    ficha(jogador, gols)

#   pt.2
def ficha(nome, gol):
    print(f'O jogador {nome}, fez {gol} gols na partida')


jogador = input('Nome do Jogador: ')
gols = input('Gols na partida: ')
if not gols.isnumeric():
    gols = 0
if jogador.strip() == '':
    jogador = 'desconhecido'
ficha(jogador, gols)

#ex.104
def leiaint(num):
    print(num)
    num = input().strip()
    while not num.isnumeric():
        print('\033[1:31mERRO! Digite um número inteiro.\033[m')
        num = input().strip()
    return num


n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')

#ex. 105   .p1
def notas(*p, sit=False):
    """
    p: uma ou mais notas
    sit: valor opcional, mostra a situação [Ruim, Razoavel ou Boa]
    return: dicionário com as informações das provas
    """
    dic = {'total': len(p), 'maior': max(p), 'menor': min(p), 'média': (sum(p)/len(p))}
    if sit:
        if dic['média'] >= 7:
            dic['situação'] = 'Boa'
        elif 5 <= dic['média'] < 7:
            dic['situação'] = 'Razoavel'
        else:
            dic['situação'] = 'Ruim'
    return dic


resp = notas(1.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)

#   pt.2
def notas(sit=False):
    notas = []
    p = 1
    while True:
        pn = float(input(f'Nota da p{p}'))
        p += 1
        notas.append(pn)
        resp = input('Outra nota?: [S/N]').lower()[0]
        if 'n' in resp:
            break
    for k, v in enumerate(notas):
        print(f'p{k+1}: {v}/ ', end='')
    dic = {'total de provas': len(notas), 'maior': max(notas), 'menor': min(notas), 'média': (sum(notas)/len(notas))}
    if sit is True:
        if dic['média'] >= 7:
            dic['situação'] = 'Boa'
        elif 5 <= dic['média'] < 7:
            dic['situação'] = 'Razoavel'
        else:
            dic['situação'] = 'Ruim'
    return dic


resp = notas(sit=True)
print()
print(resp)

#ex.106 pt.1
def comando():
    while True:
        print(30 * '=')
        print('\033[1:97:42m   Sistema de Ajuda do Pyhelp\033[m')
        print(30 * '=')
        h = input('Função ou Biblioteca: ')
        if 'fim' in h:
            break
        print(30 * '=')
        print(f'\033[1:97:44m   Acessando o manual do comando {h}\033[m...')
        print(30 * '=')
        print(f'\033[1:107m')
        print(help(h))
    print('\033[1:41m=' * 30)
    print('   Até logo!')
    print('=' * 30)
    print('\033[m')


comando()

#   pt.2
c = ('\033[m',          # 0 - sem cor
     '\033[0:30:41m',   # 1- vermelho
     '\033[0:30:42m',   # 2- verde
     '\033[0:30:43m',   # 3- amarelo
     '\033[0:30:44m',   # 4- azul
     '\033[7:30m')      # 5- branco


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[5], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('Sistema de ajuda Pyhelp', 2)
    comando = input('Função ou Biblioteca: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 1)

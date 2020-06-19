#ex. 90
aluno = dict()
aluno['nome'] = input('Digite o nome: ')
aluno['media'] = float(input('Digite a média: '))
if aluno['media'] >= 5:
    aluno['Prezado'] = 'Aprovado'
else:
    aluno['Prezado'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} ---> {v}')

#ex. 91
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(rank)
for i, v in enumerate(rank):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}.')
    sleep(0.5)

#ex.92
from datetime import date
cadastro = dict()
cadastro['nome'] = input('Nome: ')
cadastro['idade'] = date.today().year - (int(input('Ano de nascimento: ')))
cadastro['carteira'] = int(input('N° Carteira de trabalho: (0 não tem)'))
if cadastro['carteira'] != 0:
    cadastro['contrato'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salario: '))
    cadastro['aposentadoria'] = cadastro["idade"] + (cadastro['contrato'] + 35) - date.today().year
for k, v in cadastro.items():
    print(f'{k} = {v}')

#ex.93  pt.1
jogador = dict()
jogador['nome'] = input('Nome do jogador: ')
jogador['gols'] = []
p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for j in range(p):
    partida = int(input(f'Quantos gols na partida {j+1}?'))
    jogador['gols'].append(partida)
jogador['total'] = sum(jogador['gols'])
print('=' * 30)
print(jogador)
print('=' * 30)
print(f'O jogador {jogador["nome"]} jogou {p} partidas.')
for j in range(p):
    print(f'   => Na partida {j+1}, fez {jogador["gols"][j]} gols.')
print(f'Total de {jogador["total"]} gols.')

#   pt.2
jogador = dict()
partidas = list()
jogador['nome'] = input('Nome: ')
tot = int(input('Total de partidas: '))
for c in range(0, tot):
    partidas.append(int(input(f'Gols na partida {c}')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
for k, v in jogador.items():
    print(f'{k} = {v}')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador["gols"]):
    print(f' => Partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')

#ex.94
cadastro = []
pessoa = dict()
media = 0
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo: [m/f]').lower()[0]
    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']
    cadastro.append(pessoa.copy())
    resp = input('Outro cadastro? [s/n]').lower()[0]
    if 'n' in resp:
        break
print(cadastro)
print('=' * 30)
print(f'-> {len(cadastro)} pessoas foram cadastradas')
print(f'-> A média de idade é {media / len(cadastro):.1f} anos')
print(f'-> As mulheres são: ', end=' ')
for m in range(len(cadastro)):
    if 'f' in cadastro[m]['sexo']:
        print(cadastro[m]['nome'], end=' ')
print()
print(f'-> Pessoas com idade acima da média: ')
for p in range(len(cadastro)):
    if cadastro[p]['idade'] > (media / len(cadastro)):
        print(f'{cadastro[p]["nome"]} com {cadastro[p]["idade"]} anos')

#ex.95
jogadores = list()
jogador = dict()
gol = list()
tot = 0
while True:
    jogador['nome'] = input('Nome do jogador: ')
    p = int(input('Quantas partidas jogadas? '))
    for g in range(p):
        partida = int(input(f'Gols no {g+1}° jogo= '))
        gol.append(partida)
        jogador['gols'] = gol[:]
        tot += partida
    gol.clear()
    jogador['total'] = tot
    jogadores.append(jogador.copy())
    tot = 0
    resp = input('Outro jogador? [s/n]').lower()[0]
    if 'n' in resp:
        break
print(jogadores)
print('-' * 40) #cabeçalho
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(jogadores):
    print(f'{k:>2} ', end='')
    for w in v.values():
        print(f' {str(w):<15}', end='')
    print()
while True:
    print('-' * 40)
    dados = int(input('Mostrar dados de qual jogador? [999 para parar]'))
    if dados == 999:
        break
    print(f' Levantamento de {jogadores[dados]["nome"]}:')
    for d in range(len(jogadores[dados]["gols"])):
        print(f'No jogo {d+1} fez {jogadores[dados]["gols"][d]} gols.')
print('FIM!!!')

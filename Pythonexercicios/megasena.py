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

import emoji
import random
from time import sleep
print('Vamos jogar Jokenpo')
player = int(input('Pedra(1), Papel(2) ou Tesoura(3)?\n'))
pedra = 1
papel = 2
tesoura = 3
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('='*25)
pc = random.choice([1, 2, 3])
if player == pc:
    if player == 1:
        print(emoji.emojize(f':facepunch: X :facepunch: ---> Empate!!!', use_aliases=True))
    elif player == 2:
        print(emoji.emojize(f':raised_hand: X :raised_hand: ---> Empate!!!', use_aliases=True))
    elif player == 3:
        print(emoji.emojize(f':v: X :v: ---> Empate!!!', use_aliases=True))
elif player == 1 and pc == 3: #pedra x tesoura
    print(emoji.emojize(f':facepunch: X :v: ---> Derrota!!!', use_aliases=True))
elif player == 1 and pc == 2: #pedra x papel
    print(emoji.emojize(f':facepunch: X : :raised_hand:---> Derrota!!!', use_aliases=True))
elif player == 2 and pc == 3: #papel x tesoura
    print(emoji.emojize(f':raised_hand: X :v: ---> Detorrota!!!', use_aliases=True))
elif player == 2 and pc == 1: #papel x pedra
    print(emoji.emojize(f':raised_hand: X :facepunch: ---> Vitoria!!!', use_aliases=True))
elif player == 3 and pc == 1: #tesoura x pedra
    print(emoji.emojize(f':v: X :facepunch: ---> Derrota!!!', use_aliases=True))
elif player == 3 and pc == 2: #tesoura x papel
    print(emoji.emojize(f':v: X :raised_hand: ---> Vitoria!!!', use_aliases=True))
else:
    print('Coloque uma opção valida')
print('='*25)

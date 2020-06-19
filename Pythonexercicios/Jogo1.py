from time import sleep
from random import randint
print('-=-'*15)
print('O computador escolheu um numero entre \033[31m0\033[m e \033[31m5\033[m')
num = randint(0, 5)
resposta = int(input('\033[32m--->\033[mQual numero é?\033[32m<---\033[m\n'))
print('Processando...')
sleep(2)
if resposta == num:
    print(f'Parabens, a resposta  \033[31m{resposta}\033[m é igual a do computador')
else:
    print(f'O computador ganhou, a resposta era \033[31m{num}\033[m')
print('-=-'*15)

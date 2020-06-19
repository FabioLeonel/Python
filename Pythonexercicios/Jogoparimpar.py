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

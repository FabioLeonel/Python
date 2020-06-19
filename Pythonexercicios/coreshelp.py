#Help com cores
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

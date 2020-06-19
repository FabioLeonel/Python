#AULA 23 (está na pasta modulos)
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro, digite um numero Inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\nO usuario prefiriu não digitar esse numero')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro, digite um numero Real válido\033[m')
            continue
        except KeyboardInterrupt:
            print('O usuário proferiu não digitar')
            return 0
        else:
            return n


inteiro = leiaint('Digite um numero Inteiro: ')
real = leiafloat('Digite um numero Real: ')
print(f'Você digitou {inteiro} e {real}')

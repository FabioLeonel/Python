# 16
import math
n1 = float(input('numero real: '))
print(f'O numero inteiro é {math.trunc(n1)}')

# 17
from math import hypot
ca = float(input('cateto adjacente: '))
co = float(input('cateto oposto: '))
print(f'O comprimento da hipotenusa é {hypot(ca, co):.2f}')

# 18
from math import radians, sin, cos, tan
angulo = float(input('angulo: '))
print(f'seno: {sin(radians(angulo)):.2f}\ncosseno: {cos(radians(angulo)):.2f}\ntangente: {tan(radians(angulo)):.2f}')

# 19
import random
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
list = [a1, a2, a3]
print(f'O escolhido foi {random.choice(list)}')

# 20   = usa o shuffle para ebaralhar a lista, ele vem antes do print
import random
print('Lucas, Fabio e Jose')
randomlist = ['Lucas', 'Fabio', 'Jose']
random.shuffle(randomlist)
print(f'A ordem de apresentação é {randomlist}')

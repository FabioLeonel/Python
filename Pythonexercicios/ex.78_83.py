# Aula 17
#ex. 78
list1 = []    #pt.1
for li in range(5):
    list1.append(int(input('Digite um valor')))
print(list1)
print(f'O maior valor foi {max(list1)} na posição {list1.index(max(list1))} e o menor foi {min(list1)}'
      f' na posição {list1.index(min(list1))}')

#   pt.2
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input('Digite um numero: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(f'O maior é {mai} na posição ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print(f'\nO menor valor foi {men} na posição ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')

#ex.79
list2 = []
while True:
    v2 = int(input('Digite um valor: '))
    if v2 not in list2:
        list2.append(v2)
    else:
        print(f'{v2} já está na lista, ele não foi adicionado')
    r2 = input('Outro numero?: [S/N]').lower()[0]
    while r2 not in 'sn':
        r2 = input('Responda com S ou N')
    if 'n' in r2:
        break
list2.sort()
print(list2)

#ex.80      pt.1
list3 = []
for v3 in range(5):
    l3 = int(input('Digite um valor: '))
    if v3 == 0 or l3 >= list3[-1]:
        list3.append(l3)
    elif list3[0] < l3 < list3[-1]:
        if l3 <= list3[1]:
            list3.insert(1, l3)
        elif l3 <= list3[2]:
            list3.insert(2, l3)
        elif l3 >= list3[-2]:
            list3.insert(-1, l3)
    elif l3 <= list3[0]:
        list3.insert(0, l3)
    print(list3)

#   pt.2
lista = []
for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores em ordem foram {lista}')

#ex.81
list4 = []
while True:
    list4.append(int(input('Digite um numero: ')))
    r4 = input('Outro numero? [S/N]')
    while r4 not in 'sn':
        r4 = input('Outro numero? [S/N]').lower()[0]
    if 'n' in r4:
        break
list4.sort(reverse=True)
print(f'{len(list4)} numeros digitados')
print(f'Lista decrescente:\n{list4}')
if 5 in list4:
    for i, v in enumerate(list4):
        print(f'5 foi digitado')
else:
    print('5 não foi digitado')

#ex.82  pt.1
list5 = []
par = []
impar = []
while True:
    v5 = int(input('Digite um numero: '))
    list5.append(v5)
    r5 = input('Outro numero? ').lower()[0]
    if r5 in 'n':
        break
    if v5 % 2 == 0:
        par.append(v5)
    if v5 % 2 != 0:
        impar.append(v5)
print(list5)
print(par)
print(impar)

#   pt.2
num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um valor: ')))
    resp = input('Continuar? s/n ')
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Pares: {pares} \nImpares: {impares}')

#ex.83
o = []
y = list(input('Digite uma expressão: '))
for c in y:
    if c == '(':
        o.append('(')
    elif c == ')':
        o.append(')')
if o[-1] == '(':             #se o ultimo esta errado
    print('Expressão está errada')
elif y.index(')') < y.index('('):       #se o primeiro esta errado
    print('Expressão está errada')
elif y.count('(') == y.count(")"):     #se a quantidade está igual
    print('Expressão correta')
else:
    print('Expressão está errada')
print(o)

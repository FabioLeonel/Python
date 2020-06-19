# Aula 16
# ex.72
contagem = ('zero', 'one', 'two', 'three', 'for', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
            'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
    teclado = int(input('Degite um numero: '))
    if 0 <= teclado <= 20:
        break
    print(contagem[teclado])

#ex. 73
tabela = ('Botafogo', 'Corinthians', 'Flamengo', 'Fluminense', 'São Paulo', 'Coritiba', 'Atletico-MG', 'Athletico-PR',
          'Santos', 'Palmeiras', 'Goias', 'Vasco', 'Inter', 'Fortaleza', 'Bragantino', 'Gremio', 'Sport', 'Bahia',
          'Ceara', 'Atletico-Go')
print(f'Os 5 primeiros colocados são: \n{tabela[:5]}')
print(f'Os 4 ultimos são:\n {tabela[-4:]}')
print(f'Times em ordem alfabetica: \n{sorted(tabela)}')
print(f'O Corinthians está na {(tabela.index("Corinthians") + 1)}° posição')

#ex.74
from random import randint
r1 = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores foram: ', end='')
for n in r1:
    print(f'{n} ', end='')
print(f'\nO maior valor é {max(r1)}')
print(f'O menor valor é {min(r1)}')

# ex. 75
tupla1 = (int(input('Coloque um valor: ')), int(input('Coloque um valor: ')), int(input('Coloque um valor: ')),
          int(input('Coloque um valor: ')))
print(tupla1)
if 9 in tupla1:
    print(f'O valor 9 apareceu {tupla1.count(9)} vezes')
else:
    print('O 9 não apareceu')
if 3 in tupla1:
    print(f'O valor 3 foi digitado primeiro na posição {tupla1.index(3) + 1}')
else:
    print('O valor 3 não foi digitado')
print(f'Os numeros pares são:', end=' ')
for list in tupla1:
    if list % 2 == 0:
        print(f'{list}', end=' ')
if list % 2 != 0:
    print('Não tem pares')

# ex.76   pt.1
print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 30)
produtos = ('café', 1.25, 'leite', 3.50, 'pão', 5.20, 'queijo', 4.75, 'frango', 10.90)
produto = produtos[::2]
preço = produtos[1::2]
for lista in range(0, len(preço)):
    print(f'{produto[lista]:.<23}$ {preço[lista]:7.2f}')
print('-' * 30)

#   pt. 2
produtos = ('café', 1.25, 'leite', 3.50, 'pão', 5.20, 'queijo', 4.75, 'frango', 10.90)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<23}', end='')
    else:
        print(f'${produtos[pos]:>7.2f}')

#   pt. 3
produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
for c in range(0, len(produtos), 2):
    print(f"{produtos[c]:.<40} R$ {produtos[c + 1]:>7.2f}")

#. ex. 77
varias = 'carrapato', 'cachorro', 'rinoceronte', 'loja', 'remedio'
for vogais in varias:
    print(f'\nNa palavra "{vogais}" temos: ', end='')
    for vogal in vogais:
        if vogal in 'aeiou':
            print(vogal, end=' ')
 # print(f'{"a " * varias[0].count("a")}')

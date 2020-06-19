# 22
nome1 = str(input('Seu nome: ')).strip()
print(nome1.lower())
print(nome1.upper())
print(f'tem {len(espaço) - nome1.count(" ")} letras')
primeiro = nome1.split()
print(f'primeiro nome é {primeiro[0]} e tem {len(primeiro[0])} letras')

# 23 pt.1 com str
numer = int(input('Digite um numero: '))
numero = str(numer)
if len(numero) == 4:
    print(f'unidade: {numero[3]}\ndezena: {numero[2]}\ncentena: {numero[1]}\nmilhar: {numero[0]}')
if len(numero) == 3:
    print(f'unidade: {numero[2]}\ndezena: {numero[1]}\ncentena: {numero[0]}')
if len(numero) == 2:
    print(f'unidade: {numero[1]}\ndezena: {numero[0]}')
if len(numero) == 1:
    print(f'unidade: {numero[0]}')

#   pt.2 int  %para pegar o resto
num = int(input('Numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')

# 24 pt.1
cidade = input('Nome da cidade: ').strip()
if 'Santo' in cidade.split()[0].capitalize():
    print('A cidade começa com Santo')
else:
    print('a cidade não começa com Santo')

#   pt.2
cidade1 = str(input('Nome da cidade: ')).strip()
print(cidade1[:5].upper() == 'SANTO')

# 25
nome2 = str(input('Nome: ').strip())
if 'silva' in nome2.lower():
    print('tem Silva no nome')
else:
    print('Não tem Silva no nome')

#26
frase = str(input('coloque a frase: ')).strip()
print(frase.count('A'))
print(f'aparece na posição {frase.find("A")+1} primeiro')
print(f'aparece na posição {frase.rfind("A")+1} por ultimo')

#27
nome3 = input('nome: ').strip()
inteiro = nome3.split()
print(f'o primeiro nome é {inteiro[0]}\no último nome é {inteiro[-1]}')

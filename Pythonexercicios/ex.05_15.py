# ex.5
n1 = int(input('Numero '))
print('O numero é {}, o antecessor é {} e o sucessor é {}'.format(n1, n1-1, n1+1))

# ex.6
n2 = int(input('Numero '))
print(f'O numero é {n2}, o dobro é {n2*2} e a raiz é {n2**(1/2):.2f}')
# ex.7
p1 = int(input('p1= '))
p2 = int(input('p2= '))
print('A sua média é {}'.format((p1+p2)/2))

# ex. 8
m=int(input('Metros: '))
print(f'{m}m é {m*100}cm e {(m*100)*10:.0f}mm')

# ex.9
tabuada = int(input('tabuada do '))
print('-'*10)
for cont in range(1, 11):
    print(f'{tabuada} x {cont:2} ={tabuada*(cont)}')
print('-'*10)

# ex.10
carteira = float(input('Dinheiro na carteira: '))
dolar = carteira/5.29
print(f'{carteira}R$ são {dolar:.2f}US$')

# ex.11
l = float(input('Largura: '))
a = float(input('Altura: '))
print(f'A parede tem {l}m de largura e {a}m de altura \n Então sua área é {l*a}m² \n Se 1l de tinta pinta 2m², precisa-se de {(l*a)/2}l de tinta para pintar a parede')

# ex.12
preço = float(input('Preço: '))
novo = preço - (preço * 5/100)
print(f'Custo: {preço:.2f}. Com desconto de 5% é: {novo:.2f}')

# ex.13
salario = float(input('Salario: '))
aumento = float(salario*(15/100))
print(f'Seu novo salario é {salario+aumento:.2f} R$ com {aumento:.2f} R$ de aumento')

# ex.14
temperatura = float(input('Temperatura:'))
fh = temperatura * 9/5 + 32
print(f'{temperatura}C° são {fh}F°')

# ex.15
dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
pagar = dias * 60 + km * 0.15
print(f'Total a pagar {pagar} R$')

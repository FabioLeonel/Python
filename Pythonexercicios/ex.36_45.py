# ex.36
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salario? '))
anos = int(input('Quantos anos pretende pagar? '))
prestação = casa / (anos * 12)
if prestação <= salario * 0.3:
    print(f'A prestação é de {prestação:.2f}$')
else:
    print(f'O salario não é suficiente para o empréstimo')

# ex.37
import math
num = int(input('Escolha um numero inteiro:'))
base = int(input('Base de conversão:\n1-binário\n2-octal\n3-hexadecimal\n '))
if base > 3:
    print('Base de conversão incorreta')
elif base == 1:
    print(f'O valor binário de {num} é {bin(num)[2:]}')
elif base == 2:
    print(f'O valor octal de {num} é {oct(num)[2:]}')
elif base == 3:
    print(f'O valor hexadecimal de {num} é {hex(num)[2:]}')
else:
    print('Opção invalida')

# ex.38
num1 = int(input('1° numero: '))
num2 = int(input('2° numero: '))
if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1 < num2:
    print(f'{num2} é maior que {num1}')
else:
    print(f'Os dois são iguais')

# ex.39
from datetime import date
idade = int(input('Ano de nascimento: '))
if date.today().year - idade < 18:
    print(f'Você precisa se alistar em {18 - (date.today().year - idade)} anos')
    print(f'Seu alistamento será em {date.today().year + (18-(date.today().year - idade))}')
elif date.today().year - idade == 18:
    print(f'Você já tem 18 anos, aliste-se!!!')
else:
    print(f'Já passou {(date.today().year - idade) - 18} anos do prazo!!!')

# ex. 40
p1 = float(input('Nota p1: '))
p2 = float(input('Nota p2: '))
if ((p1 + p2) /2) < 3.0:
    print(f'Prezado, sua média é {(p1 + p2) /2:.2f}. Reprovado')
elif ((p1 + p2) /2) >= 5.0:
    print(f'Prezado, sua média é {(p1+p2) /2:.2f}. Aprovado')
else:
    print(f'Prezado, sua média é {(p1+p2) /2:.2f}. Recuperação')

# ex.41
from datetime import date
idad = int(input('Em que ano você nasceu? '))
data = date.today().year
if data - idad <= 9:
    print(f'{data-idad} anos. Categoria Mirim')
elif data - idad in range(10, 14):
    print(f'{data-idad} anos. Categoria Infantil')
elif data - idad in range(15, 19):
    print(f'{data-idad} anos. Categoria Junior')
elif data - idad == 20:
    print(f'{data - idad} anos. Categoria Senior')
elif data - idad > 20:
    print(f'{data-idad} anos. Categoria Master')

# ex.42
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r2 - r3 < r1 < r2 + r3 and r1 - r3 < r2 < r1 + r3 and r1 - r2 < r3 < r1 + r3:
    if r1 == r2 == r3:
        print(f'É possivel montar um triangulo equilátero, pois todas as retas são iguais')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print(f'É possivel montar um triangulo isósceles, pois tem duas retas iguais')
    elif r1 != r2 != r3 != r1:
        print(f'É possivel montar um triangulo eescaleno, pois todas as retas são diferentes')
else:
    print(f'Não é possivel montar um triangulo')

# ex.43
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}, você está abaixo do peso')
elif 18.5 <=imc < 25:
    print(f'Seu IMC é {imc:.1f}, peso ideal')
elif 25 <=imc <= 30:
    print(f'Seu IMC é {imc:.1f}, Sobrepeso')
elif 30 <= imc <= 40:
    print(f'Seu IMC é {imc:.1f}, Obesidade')
elif imc >= 40:
    print(f'Seu IMC é {imc:.2f}, Obesidade morbida')

# ex.44
preço = float(input('Preço do produto: '))
pagamento = int(input('''Formas de pagamento
[ 1 ] Dinheiro 
[ 2 ] Cartão 
[ 3 ] x2
[ 4 ] x3 ou mais'''))
dinheiro = preço * 0.10
cartão = preço * 0.05
x2 = preço
x3 = preço * 0.20
if pagamento == 1:
    print(f'{dinheiro:.2f}$ de desconto\nPreço final: {preço-dinheiro:.2f}$')
elif pagamento == 2:
    print(f'{cartão:.2f}$ de desconto\nPreço final: {preço-cartão:.2f}$')
elif pagamento == 3:
    print(f'{preço - x2:.2f}$ de desconto\nPreço final: {x2:.2f}$')
elif pagamento == 4:
    total = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {total}x de {preço / total:.2f}$')
    print(f'{x3:.2f}$ de juros\nPreço final: {preço + x3:.2f}')
else:
    total = 0
    print('Opção invalida de pagamento')

# ex.45 - Jo Ken Po


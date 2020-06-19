
#ex.56
idades = []
maioridadehomem = 0
homemvelho = ''
mulher20 = 0
for p in range(1, 5):
    print(f'--{cadastro}° pessoa--')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    idades.append(idade)
    sexo = input('Sexo:\n M/F').strip().lower()
    if p == 1 and 'm':
        maioridadehomem = idade
        homemvelho = nome
    else:
        if sexo in 'm' and idade > maioridadehomem:
            maioridadehomem = idade
            homemvelho = nome
    if sexo == 'f' and idade < 20:
        mulher20 += 1
print(f'A média de idade é: {sum(idades) / len(idades)}\nO homem mais velho é: {(homemvelho).capitalize()}')
print(f'Ao todo são {mulher20} mulheres com menos de 20 anos')

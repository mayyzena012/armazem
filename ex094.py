#aqui voce coloca sua mae

cadastro = {}
lista = []

while True:
    cadastro['nome'] = input('Digite seu nome: ')

    while True:
        sexo = input('Digite seu sexo M/F: ').upper()[0]
        if sexo in 'MF':
            break
        else:
            print('Incorreto.')

    cadastro['sexo'] = sexo
    cadastro['idade'] = int(input('Digite sua idade: '))
    perg = input('Quer continuar? [S/N] ').upper()[0]
    lista.append(cadastro.copy())

    if perg == 'N':
        break
    
#parei aqui
for idade in lista:
    print(idade[0][2])


print(cadastro)
print(lista)

print(f'A quantidade de pessoas cadastradas foi {len(lista)}')
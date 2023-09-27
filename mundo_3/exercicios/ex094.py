#aqui voce coloca sua mae

#listas que recebem os valores
pessoa = {}
lista_pessoas = []
lista_mulheres = []
pessoa_acima_idade = []
# a soma
soma_idade= 0

while True:
    pessoa['nome'] = input('Digite seu nome: ')

    while True:
        pessoa['sexo'] = input('Digite seu sexo M/F: ').upper()[0]
       
        if pessoa['sexo'] in 'MF':
            break 
        else:
            print('Incorreto.')

    pessoa['idade'] = int(input('Digite sua idade: '))
    soma_idade += pessoa['idade']
    
    continuar = input('Quer continuar? [S/N] ').upper()[0]
    lista_pessoas.append(pessoa.copy())
    
    if pessoa['sexo'] == 'F':
        lista_mulheres.append(pessoa['nome'])

    if continuar == 'N':
        break
    
media = soma_idade / len(lista_pessoas)
# 1 - encontre a media da idade do grupo
print(f'A media da idade das pessoas e {media}')
print('-='*40)

# 2 - uma lista com todas as mulheres
print(f'As mulheres cadastradas sao: ',end= '')
for mulher in lista_mulheres:
    print(mulher, end=' ')
print('')
print('-='*40)

# 3 - uma lista com as pessoas acima da media de idade
for pessoa in lista_pessoas:
    idade_pessoa = pessoa['idade']
    if idade_pessoa > media:
        pessoa_acima_idade.append(pessoa)

print('Lista de pessoas acima da media ', end='')
for pessoa_acima in pessoa_acima_idade:
    print(f'Nome = {pessoa_acima["nome"]}; sexo = {pessoa_acima["sexo"]}; idade = {pessoa_acima["idade"]}')

print('-='*40)
print(f'A quantidade de pessoas cadastradas foi {len(lista_pessoas)}')
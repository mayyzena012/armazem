#

galera = list()
dados = list()
maior = menor = 0
while True:
    dados.append(input('Digite seu nome: '))
    dados.append(int(input('Digite seu peso: ')))
    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    galera.append(dados[:])
    dados.clear()
    r = input('Vce quer continuar [S/N]? ').upper()
    if r == 'N':
        break


print(f'A quantidade de pessoas cadastrada foi {len(galera)}')
print(f'O maior peso foi {maior} de', end=' ')
for p in galera:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'o menor peso foi {menor} de', end=' ')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')



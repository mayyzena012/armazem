#
total = mil = 0 
preco_menor = float('inf')
nome_menor = ''
while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preco do produto: '))
    while True:
        c = input('voce quer continuar S/N? ').upper()
        if c == 'S'or'N':
            break
        else:
            print('Invalido. Digite novamente')
    total += preco
    if preco > 1000:
        mil += 1
    elif preco < preco_menor:
            preco_menor = preco
            nome_menor = nome
    if c == 'N':
            break

print('----------- COMPRA FINALIZADA -----------')
print(f'voce gastou um total de R${total:.2f}. {mil} produtos custam mais de R$1000.\n e o produto mais barato foi {nome_menor} no valor de R${preco_menor:.2f}')
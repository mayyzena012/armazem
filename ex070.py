#
total = mil = 0
while True:
        nome = input('Nome do produto: ')
        preco = float(input('Preco do produto: '))
        c = input('voce quer continuar S/N? ').upper()

        total += preco
        print(total)
        print(mil)
        if preco > 1000:
            mil += 1
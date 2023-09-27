#

valores = list()

while True:
    valor = int(input('Digite um numero '))
    if valor in valores:
        print('Numero duplicado digite outro numero ')
    else:
        valores.append(valor)
    while True:
        p = input('Voce quer continuar [S/N]? ').upper()[0]
        if p == 'S' or 'N':
            break

    if p == 'N':
        break

print('programa encerrado')
valores.sort()
print(f'Voce digitou os valores {valores}')

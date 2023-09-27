#

valores = list()

while True:
    valores.append(int(input('Digite um valor ')))
    while True:
        s = str(input('voce quer continuar [S/N]? ')).upper()[0]
        if s == 'S' or 'N':
            break

    if s == 'N':
        break


valores.sort(reverse=True)
print(f'Voce digitou [{len(valores)}] valores e eles sao {valores}')
if 5 in valores:
    print(f'o valor 5 esta na lista na posicao {valores.index(5)}')
else:
    print('O valor 5 nao esta na lista.')

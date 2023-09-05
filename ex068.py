#
from random import randrange

cont = 0

print('='*20)
print('JOGO DE PAR OU IMPAR')
print('='*20)
while True:
    pc = randrange(50)
    num = int(input('Digite um valor '))
    eu = input('Digite se esse numero e PAR ou IMPAR ').strip().lower()
    soma = num + pc
    par = soma % 2
    impar = soma % 2
    if eu == 'par':
        if par == 0:
            cont += 1
            print('-'*40)
            print(f'Voce jogou {num} e o computador jogou {pc}')
            print('-'*40)
            print(f'VOCE ACERTOU! a soma e {soma} DEU PAR!')
            print('-'*40)
        else:
            print(f'Voce errou, o jogo acabou, o numero {soma} nao e um numero PAR. Voce acertou {cont} vezes')
            break
    if eu == 'impar':
        if impar == 1:
            cont += 1
            print('-'*40)
            print(f'Voce jogou {num} e o computador jogou {pc}')
            print('-'*40)
            print(f'VOCE ACERTOU! a soma e {soma} DEU IMPAR!')
            print('-'*40)
        else:
            print(f'GAME OVER!! voce errou, o numero {soma} nao e um numero IMPAR. Voce acertou {cont} vezes')
            break
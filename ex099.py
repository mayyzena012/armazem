#ex099 quase 100

def maior(*args):
    maior = 0
    print(' valores passandos sao esses ', end = '')
    for valor in args:
        print(f'{valor}', end='')
    print(f' \n A  quantidade foi {len(args)}')
    if len(args) == 0:
        print(f'Maior {maior}')
    else:
        maior = max(args)
        print(f'Maior {maior}')


maior(6,7,3,4,5,)
maior(1,2,5,9)
maior(5,6,7)

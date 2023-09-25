#

def fatorial(num, show=False):
    fator = 1
    for v in range(num, 0, -1):
        print(v, end='')
        if show:
            if v > 1:
                print(' x ',end='')
            else:
                print(' = ' ,end='')
            fator *= v
    return fator

num = int(input('Valor: '))
print(fatorial(num, show=True))
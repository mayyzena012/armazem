#

def fatorial(num, show=False):
    """
    -> calcula o fatorial de um numero.
    :parem n: O numero a ser calculado.
    :parem show: (opcional) mostra o calculo sim ou nao.
    :return: Retorna o fatorial do numero inserido.
    """
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